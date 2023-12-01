from auth import SHEETY_BEARER_TOKEN
from sensitive import SHEETY_PRIVATE_ENDPOINT_PRICES
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.BEARER_TOKEN = SHEETY_BEARER_TOKEN
        self.ENDPOINT = SHEETY_PRIVATE_ENDPOINT_PRICES

    def get_sheet_content(self):
        response = requests.get(url=self.ENDPOINT, auth=BearerAuth(self.BEARER_TOKEN))
        response.raise_for_status()
        print(response.status_code)
        return response.json()
        # debug below
        # return {'prices': [{'city': 'Paris', 'iataCode': 'd', 'lowestPrice': 54, 'id': 2},
        # {'city': 'Berlin', 'iataCode': 'd', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'd',
        # 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'd', 'lowestPrice': 551, 'id': 5},
        # {'city': 'Istanbul', 'iataCode': 'd', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '',
        # 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
        # {'city': 'San Francisco', 'iataCode': 'd', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode':
        # '', 'lowestPrice': 378, 'id': 10}]}

    def get_iata_codes(self):
        # TODO search for the actual string
        return "TESTING"

    def update_sheet_row(self, row_id, change_json):
        edit_endpoint = self.ENDPOINT + f"/{row_id}"
        response = requests.put(url=edit_endpoint, auth=BearerAuth(self.BEARER_TOKEN), json=change_json)
        response.raise_for_status()
        print(response.status_code)


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
