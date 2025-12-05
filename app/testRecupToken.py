import requests
import json

BASE_URL = "http://127.0.0.1:8000"
TOKEN_ENDPOINT = "/api/v1/supervision/token"

USERNAME = "root@gmail.com"
PASSWORD = "bonjour"

token_data = {
    "username": USERNAME,
    "password": PASSWORD
}

response = requests.post(
    f"{BASE_URL}{TOKEN_ENDPOINT}",
    data=token_data  # form-data pour OAuth2PasswordRequestForm
)

try:
    response.raise_for_status()
    print("Réponse JSON :")
    print(json.dumps(response.json(), indent=4))
except requests.exceptions.HTTPError as e:
    print(f"Erreur HTTP : {e} - {response.text}")
except json.decoder.JSONDecodeError:
    print(f"Réponse non JSON : {response.text}")
