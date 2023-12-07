from auth import SHEETY_BEARER_TOKEN
from sensitive import SHEETY_PRIVATE_ENDPOINT_USERS
import requests

def post_new_row(firstname, lastname, email):
    header = {
        "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
        "Content-Type": "application/json",
    }

    json = {
        "user": {
            "firstName": firstname,
            "lastName": lastname,
            "email": email,
        }
    }

    response = requests.post(url=SHEETY_PRIVATE_ENDPOINT_USERS, headers=header, json=json)
    response.raise_for_status()
    print(response.text)
    return response.status_code