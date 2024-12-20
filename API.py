import json
import requests
from datetime import datetime

date = datetime.today()


def fetch_actual_data():
    endpoint = f"https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/?date={date}"
    data = requests.get(endpoint).json()

    with open("rates.json", "w") as file:
        file.write(json.dumps(data, indent=4))

    return file


def fetch_specific_data(currency):
    endpoint = f"https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/?currencies={currency}&date={date}"
    data = requests.get(endpoint).json()

    return data



