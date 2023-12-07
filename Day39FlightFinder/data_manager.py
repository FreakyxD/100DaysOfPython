from auth import SHEETY_BEARER_TOKEN
from sensitive import SHEETY_PRIVATE_ENDPOINT_PRICES, SHEETY_PRIVATE_ENDPOINT_USERS
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

    def update_sheet_row(self, row_id, change_json):
        edit_endpoint = self.ENDPOINT + f"/{row_id}"
        response = requests.put(url=edit_endpoint, auth=BearerAuth(self.BEARER_TOKEN), json=change_json)
        response.raise_for_status()
        print(response.status_code)

    def get_customer_emails(self):
        customer_endpoint = SHEETY_PRIVATE_ENDPOINT_USERS
        response = requests.get(customer_endpoint, auth=BearerAuth(self.BEARER_TOKEN))
        response.raise_for_status()
        return response.json()["users"]


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
