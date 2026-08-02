import requests
from config import API_KEY

BASE_URL = f"https://v6.exchangerate-api.com/v6/"

def convert_currency(from_currency, to_currency, amount):
    url = f"{BASE_URL}/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None