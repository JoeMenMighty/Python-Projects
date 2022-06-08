# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint

FLIGHT_DEAL_SHEET_API = "https://api.sheety.co/38992ecbc793bcad3a069267f1eadb31/flightDeals/prices"


flight_data_response = requests.get(url=FLIGHT_DEAL_SHEET_API)
flight_data_response.raise_for_status()
sheet_data = list(flight_data_response.json()['prices'])
pprint(sheet_data)
