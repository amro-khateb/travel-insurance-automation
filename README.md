# TRAVEL HEALTH INSURANCE

🛡️ Travel Health Insurance - Process Automation with Camunda 8

This repository contains the complete end-to-end automation of an application process for travel health insurance. The project impressively demonstrates the seamless integration of model-driven process orchestration (BPMN), complex decision logic (DMN), and modern microservice architectures (Python Zeebe Workers & REST-APIs).
Developed by Team G1 at TU Dortmund.

## 📑 Table of Contents

* Project Description
* Highlights & Features
* Technology Stack
* Architecture & Project Structure
* Business Logic (DMN)
* Human-in-the-Loop
* Installation & Setup

---

## 📖 Project Description

The goal of this project is the transformation of a manual, time-consuming insurance process into a highly efficient, automated workflow. Once a customer submits an application, it is processed entirely digitally. This includes the validation of travel data, currency conversion, credit and security checks, partner data management (search and creation), as well as final policy issuance and the dispatch of contract documents.

---

## ✨ Highlights & Features

* **Straight-Through Processing (STP):** Error-free applications go through the process fully automated in just a few seconds.
* **API-First Approach:**
* **External APIs:** Integration of the Frankfurter API (currency conversion), API-Ninjas (phone number validation), and the Federal Foreign Office (travel warnings).
* **Internal APIs:** Integration of simulated backend systems for partner management (Partner-API) and contract management (Insurance-Policy-API).


* **Out-of-the-Box Connectors:** Utilization of native Camunda Connectors (HTTP JSON, SendGrid/Mailtrap) for efficient API calls and automated email communication.
* **Fault Tolerance:** Integrated retry mechanisms and timeouts (e.g., in case of API failures).

---

## 🛠️ Technology Stack

* **Process Engine:** Camunda 8 Cloud (SaaS)
* **Modeling:** Camunda Web Modeler (BPMN 2.0, DMN 1.3, Camunda Forms)
* **Backend / Worker:** Python 3.10+
* **Zeebe Client:** pyzeebe
* **Communication:** RESTful APIs, gRPC (Zeebe)

---

## 🏗️ Architecture & Project Structure

The business logic is decoupled from the process flow. Camunda Cloud orchestrates the workflow, while the Python worker running locally (or in the cloud) executes the actual service tasks.

```text
📦 reisekrankenversicherung
 ┣ 📂 models/                 # Camunda Models
 ┃ ┣ 📜 reisekrankenversicherung_prozess.bpmn
 ┃ ┣ 📜 Alter_Wohnort_Personen_pruefen.dmn
 ┃ ┣ 📜 Selbstbehalt_bestimmen.dmn
 ┃ ┗ 📜 *.form                # Camunda Forms (User Interfaces)
 ┣ 📂 src/                    # Python Worker Code
 ┃ ┣ 📜 main.py               # Entry point, starts Worker & Cloud-Channel
 ┃ ┣ 📜 config.py             # Configuration file (Credentials, URLs)
 ┃ ┣ 📜 tasks.py              # Registration of Camunda Service Tasks (@worker.task)
 ┃ ┣ 📜 partner_api.py        # Logic for the Partner System (Search/Create)
 ┃ ┣ 📜 insurance_api.py      # Logic for Contract Storage & Document Dispatch
 ┃ ┗ 📜 utils.py              # Helper functions (e.g., Data Normalization)
 ┗ 📜 README.md

```
