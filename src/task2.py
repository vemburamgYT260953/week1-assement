
import csv
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

load_dotenv(ROOT / ".env")
api_key = os.getenv("API_KEY")

# CSV and JSON
with open(DATA / "employees.csv", newline="", encoding="utf-8") as file:
    employees = list(csv.DictReader(file))

for emp in employees:
    emp["id"] = int(emp["id"])
    emp["salary"] = float(emp["salary"])

with open(DATA / "employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

high_earners = [emp for emp in employees if emp["salary"] > 50000]

with open(DATA / "high_earners.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(high_earners)

print(f"Rows read: {len(employees)} | High earners: {len(high_earners)}")

# Calling API 
url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    users = response.json()

    for user in users[:3]:
        print(f'{user["id"]} - {user["name"]} - {user["email"]}')

    first_company = users[0].get("company", {})
    company_name = first_company.get("name", "Unknown")

    result = {
        "first_user": users[0].get("name"),
        "company_name": company_name,
        "users": users
    }

    with open(DATA / "users.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

except requests.exceptions.Timeout:
    print("API request timed out.")
except requests.exceptions.ConnectionError:
    print("Unable to connect to the API.")
except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)
except (ValueError, KeyError, IndexError) as error:
    print("Invalid API response:", error)

# Testing the 404 endpoints 
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        response.raise_for_status()
        print("Unexpected response:", response.status_code)

except requests.exceptions.Timeout:
    print("404 test timed out.")
except requests.exceptions.ConnectionError:
    print("Connection failed during 404 test.")
except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)
