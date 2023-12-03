import requests
from datetime import datetime, timedelta
from auth import FLIGHT_SEARCH_API_KEY
from sensitive import DEPARTURE_IATA


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.API_KEY = FLIGHT_SEARCH_API_KEY
        self.ENDPOINT = "https://api.tequila.kiwi.com"
        self.DEPARTURE = DEPARTURE_IATA
        self.headers = {
            "apikey": self.API_KEY
        }

    def get_iata_codes(self, query):
        parameters = {
            "term": query,
            "location_types": "city",
            "limit": 1,
        }
        response = requests.get(url=self.ENDPOINT + "/locations/query", params=parameters, headers=self.headers)
        response.raise_for_status()
        print(response.status_code)
        return response.json()["locations"][0]["code"]

    def get_cheapest_flight(self, city_iata):
        """Uses the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for the
        provided city IATA code"""

        date_today = datetime.today()
        date_plus_6m = date_today + timedelta(weeks=24)

        parameters = {
            "fly_from": self.DEPARTURE,
            "fly_to": city_iata,
            "date_from": date_today.strftime("%d/%m/%Y"),
            "date_to": date_plus_6m.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "selected_cabins": "M",
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "EUR",
            "sort": "price",
            "limit": 1,
        }

        response = requests.get(url=self.ENDPOINT + "/search", params=parameters, headers=self.headers)
        response.raise_for_status()
        print(response.status_code)
        return response.json()
