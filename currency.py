import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']

def convert_currency(base):
    currencies = ','.join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency")
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()
    if base == 'Q':
        exit()

    amount = input("Enter the amount (q for quit ): ").upper()
    if amount == 'Q':
        exit()

    data = convert_currency(base)
    if data is None:
        print("An error occurred while fetching data")
        continue
    del data[base]
    for key, value in data.items():
        print(f"{key}: {value * float(amount):.2f}")
    