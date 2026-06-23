import asyncio
from datetime import date
import requests
from requests.auth import HTTPBasicAuth
from pyzeebe import ZeebeClient, ZeebeWorker, create_camunda_cloud_channel

API_BASE_URL = "https://travel-insurance-api.aws-playground.viadee.cloud"
API_USERNAME = "user1"
API_PASSWORD = "m7Qb2Xr9"

def search_partner_by_number(partnernummer: str):
    response = requests.get(
        f"{API_BASE_URL}/partner/{partnernummer}",
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
        timeout=10
    )
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()

def search_partner_by_data(policy_holder: dict):
    api_payload = {
        "firstName": policy_holder.get("firstname"),
        "lastName": policy_holder.get("lastname"),
        "birthDate": policy_holder.get("birthday"),
        "phoneNumber": policy_holder.get("phoneNumber", ""),
        "emailAddress": policy_holder.get("mail", "")
    }
    
    address = policy_holder.get("address", {})
    if address:
        api_payload["address"] = {
            "street": address.get("street", ""),
            "postalCode": address.get("postCode", ""),
            "city": address.get("city", "")
        }

    response = requests.post(
        f"{API_BASE_URL}/partner/search",
        json=api_payload,
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
        timeout=10
    )
    
    if response.status_code == 404:
        return None
    response.raise_for_status()
    
    try:
        data = response.json()
        if isinstance(data, list):
            return data[0] if data else None
        return data.get("partnerId") and data or None
    except ValueError:
        return None

def create_partner(policy_holder: dict):
    api_payload = {
        "firstName": policy_holder.get("firstname"),
        "lastName": policy_holder.get("lastname"),
        "birthDate": policy_holder.get("birthday"),
        "phoneNumber": policy_holder.get("phoneNumber", ""),
        "emailAddress": policy_holder.get("mail", "")
    }
    
    address = policy_holder.get("address", {})
    if address:
            api_payload["address"] = {
                "street": address.get("street", ""),
                "number": address.get("number", ""),                 
                "postalCode": address.get("postCode", ""),
                "city": address.get("city", ""),
                "countryCode": address.get("country", "")       
            }

    response = requests.post(
        f"{API_BASE_URL}/partner",
        json=api_payload,
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
        timeout=10
    )

    response.raise_for_status()
    
    raw_response = response.text.strip().replace('"', '') 
    
    if raw_response:
        print(f"Erfolgreich angelegt. Echte Partner-ID: {raw_response}")
        return {"partnerId": raw_response}
    else:
        return {"partnerId": ""}
    

def normalize(value):
    return str(value or "").lower().replace(" ", "").strip()


def addresses_match(policy_holder: dict, partner: dict):
    input_address = policy_holder.get("address", {})
    partner_address = partner.get("address", {})
    
    return (
        normalize(input_address.get("street")) == normalize(partner_address.get("street"))
        and normalize(input_address.get("postCode")) == normalize(partner_address.get("postalCode"))
        and normalize(input_address.get("city")) == normalize(partner_address.get("city"))
    )

async def main():
    channel = create_camunda_cloud_channel(
        client_id="ltwJt9mnJ5L4LQ_pNY_ok-Mrmm5ZGgXg",
        client_secret="iO_98rmtktOHI3wy0GHaw97BV55YKz7.8GIN.gJRcc.r~aeMpqIqcGLqg2lgjGEU",
        cluster_id="98230c11-3e6c-42f5-8e66-07928c4229b8",
        region="fra-1"
    )

    worker = ZeebeWorker(channel)

    @worker.task(task_type="validate-data")
    def validate_data(travelInsurance: dict):
        print("Daten validieren...")
        travel_data = travelInsurance.get("travelData", {})
        beginn = date.fromisoformat(travel_data.get("start"))
        ende = date.fromisoformat(travel_data.get("end"))
        kosten = float(travel_data.get("cost", 0))
        return {
            "datenGueltig": beginn < ende and beginn > date.today() and kosten > 0,
            "reisebeginnVorReiseende": beginn < ende,
            "reisebeginnInZukunft": beginn > date.today(),
            "reisekostenPositiv": kosten > 0
        }

    @worker.task(task_type="search-vn")
    def search_vn(travelInsurance: dict):
        print("VN im Partnersystem suchen...")
        policy_holder = travelInsurance.get("policyHolder", {})
        partnernummer = policy_holder.get("id", "")

        if not partnernummer:
            return {"partnernummerAngegeben": False}

        try:
            partner = search_partner_by_number(partnernummer)
            if partner is None:
                return {"partnernummerAngegeben": True, "partnerMitPartnernummerGefunden": False}
            
            adresse_stimmt = addresses_match(policy_holder, partner)
            return {
                "partnernummerAngegeben": True,
                "partnerMitPartnernummerGefunden": True,
                "partnernummer": partner.get("partnerId", partnernummer),
                "partnerAusApi": partner,
                "adresseStimmtUeberein": adresse_stimmt
            }
        except Exception as e:
            print("Fehler bei search-vn:", e)
            return {"partnernummerAngegeben": True, "partnerMitPartnernummerGefunden": False, "apiFehler": True}

    @worker.task(task_type="search-partner")
    def search_partner(travelInsurance: dict):
        print("Partner im System suchen...")
        try:
            partner = search_partner_by_data(travelInsurance.get("policyHolder", {}))
            if partner is None:
                return {"partnerPerSucheGefunden": False}
            return {
                "partnerPerSucheGefunden": True,
                "partnernummer": partner.get("partnerId"),
                "partnerAusApi": partner
            }
        except Exception as e:
            print("Fehler bei search-partner:", e)
            return {"partnerPerSucheGefunden": False, "apiFehler": True}

    @worker.task(task_type="create-partner")
    def create_partner_task(travelInsurance: dict):
        print("Neukundin im System anlegen...")
        try:
            partner = create_partner(travelInsurance.get("policyHolder", {}))
            new_partner_id = partner.get("partnerId", "")

            if "policyHolder" not in travelInsurance:
                travelInsurance["policyHolder"] = {}

            travelInsurance["policyHolder"]["id"] = new_partner_id

            print("Neue Partnernummer wird an Camunda zurückgegeben:", new_partner_id)

            return {
                "partnernummer": new_partner_id,
                "partnerAusApi": partner,
                "neukundinAngelegt": True,
                "travelInsurance": travelInsurance
            }

        except Exception as e:
            print("Fehler bei create-partner:", e)
            return {
                "neukundinAngelegt": False,
                "apiFehler": True
            }

    @worker.task(task_type="vertrag-speichern")
    def vertrag_speichern(travelInsurance: dict, partnernummer: str = "", Selbstbehalt: int = 0):
        print("Vertrag speichern in API...")

        p_id = partnernummer
        if not p_id:
            p_id = travelInsurance.get("policyHolder", {}).get("id", "")

        if not p_id:
            print("Keine Partnernummer gefunden!")
            return {
                "apiFehler": True,
                "vertragGespeichert": False,
                "fehlermeldung": "Keine Partnernummer gefunden"
            }

        travel_data = travelInsurance.get("travelData", {})

        insured_persons_input = travelInsurance.get("insuredPartners", [])

        insured_persons = []
        for person in insured_persons_input:
            insured_persons.append({
                "firstName": person.get("firstname", ""),
                "lastName": person.get("lastname", ""),
                "birthDate": person.get("birthday", ""),
                "childOfInsuranceTaker": person.get("childOfPolicyHolder", False)
            })

        payload = {
            "insuranceTakerId": p_id,
            "travelDetails": {
                "begin": travel_data.get("start", ""),
                "end": travel_data.get("end", ""),
                "destinationCountryCode": travel_data.get("destination", ""),
                "totalCost": int(float(travel_data.get("cost", 0))),
                "currency": travel_data.get("currency", "EUR")
            },
            "coverage": {
                "costRetention": Selbstbehalt or 0,
                "withBaggageCoverage": travelInsurance.get("baggageInsurance", False),
                "withTravelAbortionCoverage": travelInsurance.get("travelCancellation", False),
                "withTravelExtensionCoverage": False
            },
            "insuredPersons": insured_persons
        }

        try:
            print(f"Sende Payload an API: {payload}")

            response = requests.post(
                f"{API_BASE_URL}/insurance-policy",
                json=payload,
                auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
                timeout=10
            )

            print("Insurance Policy API Status:", response.status_code)
            print("Insurance Policy API Antwort:", response.text)

            if response.status_code >= 400:
                print(f"API Fehler Antwort: {response.text}")

            response.raise_for_status()

            versicherungsnummer = response.text.strip().replace('"', "")

            return {
                "versicherungsnummer": versicherungsnummer,
                "vertragGespeichert": True,
                "apiFehler": False
            }

        except Exception as e:
            print("Fehler beim Speichern des Vertrags:", e)
            return {
                "apiFehler": True,
                "vertragGespeichert": False,
                "fehlermeldung": str(e)
            }

    @worker.task(task_type="unterlagen-senden")
    def unterlagen_senden(versicherungsnummer: str = "V-UNBEKANNT"):
        print(f"Vertragsunterlagen für Vertrag {versicherungsnummer} drucken und senden...")
        try:
            response = requests.post(
                f"{API_BASE_URL}/documents/print", 
                json={"versicherungsnummer": versicherungsnummer},
                auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
                timeout=10
            )
            if response.status_code == 404:
                return {"unterlagenGesendet": True}
            response.raise_for_status()
            return {"unterlagenGesendet": True}
        except Exception as e:
            print("Fehler beim Drucken:", e)
            return {"unterlagenGesendet": True, "printWarnung": str(e)}

    print("Worker läuft mit Camunda Cloud...")
    await worker.work()

if __name__ == "__main__":
    asyncio.run(main())