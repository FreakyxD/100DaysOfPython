import requests
from auth import FLIGHT_SEARCH_API_KEY


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.API_KEY = FLIGHT_SEARCH_API_KEY
        self.ENDPOINT = "https://api.tequila.kiwi.com"

    def get_iata_codes(self, query):
        headers = {
            "apikey": self.API_KEY
        }

        parameters = {
            "term": query,
            "location_types": "city",
            "limit": 1,
        }
        response = requests.get(url=self.ENDPOINT + "/locations/query", params=parameters, headers=headers)
        response.raise_for_status()
        print(response.status_code)
        return response.json()["locations"][0]["code"]
