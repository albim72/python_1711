import requests
from requests.auth import HTTPBasicAuth

# 1. Endpoint Jiry – np. pobranie konkretnego zgłoszenia
url = "https://twoja_jira.atlassian.net/rest/api/3/issue/TEST-123"

# 2. Dane autoryzacyjne
email = "twoj_email@firma.com"
api_token = "TWÓJ_TOKEN_API"

# 3. Wysłanie zapytania
response = requests.get(url, auth=HTTPBasicAuth(email, api_token))

# 4. Odczyt JSON
if response.status_code == 200:
    data = response.json()       # <- tu masz cały JSON jako dict
    print("Pobrane dane:")
    print(data)
else:
    print(f"Error: {response.status_code}, {response.text}")


summary = data["fields"]["summary"]
status = data["fields"]["status"]["name"]

print("Tytuł:", summary)
print("Status:", status)



import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)
data = response.json()

print("ID:", data["id"])
print("Title:", data["title"])
