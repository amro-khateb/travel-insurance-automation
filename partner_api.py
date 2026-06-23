import requests
from requests.auth import HTTPBasicAuth
from config import API_BASE_URL, API_USERNAME, API_PASSWORD


def search_partner_by_number(partnernummer: str):
    # Partner direkt über die Partnernummer suchen.
    response = requests.get(
        f"{API_BASE_URL}/partner/{partnernummer}",
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
        timeout=10
    )

    # Wenn kein Partner gefunden wird, geben wir None zurück.
    if response.status_code == 404:
        return None

    # Bei anderen Fehlern soll Python eine Exception werfen.
    response.raise_for_status()

    # Antwort der API als Dictionary zurückgeben.
    return response.json()


def search_partner_by_data(policy_holder: dict):
    # Daten aus dem Antrag in das Format der Partner-API bringen.
    api_payload = {
        "firstName": policy_holder.get("firstname"),
        "lastName": policy_holder.get("lastname"),
        "birthDate": policy_holder.get("birthday"),
        "phoneNumber": policy_holder.get("phoneNumber", ""),
        "emailAddress": policy_holder.get("mail", "")
    }

    # Adresse nur mitschicken, wenn sie im Antrag vorhanden ist.
    address = policy_holder.get("address", {})
    if address:
        api_payload["address"] = {
            "street": address.get("street", ""),
            "number": address.get("number", ""),
            "postalCode": address.get("postCode", ""),
            "city": address.get("city", ""),
            "countryCode": address.get("country", "")
        }

    # Payload zur Kontrolle ausgeben.
    print("Partner-Suche Payload:", api_payload)

    # Suche über die Partner-API starten.
    response = requests.post(
        f"{API_BASE_URL}/partner/search",
        json=api_payload,
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
        timeout=10
    )


    # Wenn kein Partner gefunden wurde, ist das kein technischer Fehler.
    # Dann kann später ein neuer Partner angelegt werden.
    if response.status_code == 404:
        return None

    # Falls die API intern einen Fehler hat, brechen wir den Prozess hier nicht ab.
    # Es wird dann einfach kein Partner gefunden.
    if response.status_code >= 500:
        return None

    response.raise_for_status()

    try:
        data = response.json()

        # Die API kann eine Liste zurückgeben.
        if isinstance(data, list):
            return data[0] if data else None

        # Falls ein einzelnes Objekt zurückkommt.
        return data.get("partnerId") and data or None

    except ValueError:
        # Falls die Antwort nicht als JSON gelesen werden kann.
        return None


def create_partner(policy_holder: dict):
    # Neuen Partner aus den Daten des Versicherungsnehmers erstellen.
    api_payload = {
        "firstName": policy_holder.get("firstname"),
        "lastName": policy_holder.get("lastname"),
        "birthDate": policy_holder.get("birthday"),
        "phoneNumber": policy_holder.get("phoneNumber", ""),
        "emailAddress": policy_holder.get("mail", "")
    }

    # Adresse aus dem Formular in das Format der API umwandeln.
    address = policy_holder.get("address", {})
    if address:
        api_payload["address"] = {
            "street": address.get("street", ""),
            "number": address.get("number", ""),
            "postalCode": address.get("postCode", ""),
            "city": address.get("city", ""),
            "countryCode": address.get("country", "")
        }

    # Neuen Partner in der API anlegen.
    response = requests.post(
        f"{API_BASE_URL}/partner",
        json=api_payload,
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
        timeout=10
    )

    response.raise_for_status()

    # Die API gibt hier nur die Partner-ID als Text zurück.
    raw_response = response.text.strip().replace('"', "")

    if raw_response:
        print(f"Erfolgreich angelegt. Echte Partner-ID: {raw_response}")
        return {"partnerId": raw_response}

    return {"partnerId": ""}