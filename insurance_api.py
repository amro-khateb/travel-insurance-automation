import requests
from requests.auth import HTTPBasicAuth
from config import API_BASE_URL, API_USERNAME, API_PASSWORD


def save_insurance_policy(payload: dict):
    # Vertrag über die Insurance-Policy-API speichern.
    response = requests.post(
        f"{API_BASE_URL}/insurance-policy",
        json=payload,
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
        timeout=10
    )


    if response.status_code >= 400:
        print("API Fehler Antwort:", response.text)

    response.raise_for_status()

    # Die Versicherungsnummer kommt als Text zurück.
    return response.text.strip().replace('"', "")


def print_documents(policy_id: str):
    # Für das Drucken der Vertragsunterlagen muss die Versicherungsnummer
    # als Teil der URL an die Dokumenten-API übergeben werden.
    response = requests.post(
        f"{API_BASE_URL}/document/print-job/insurance-policy/{policy_id}",
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
        timeout=10
    )

    print("Document API Status:", response.status_code)
    print("Document API Antwort:", response.text)

    return response