import requests
from auth import NUTRITIONIX_APP_ID, NUTRITIONIX_API_KEY

NUTRITIONIX_NAT_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

parameters = {
    "query": input("Tell me which exercises you did: ")
}

response = requests.post(url=NUTRITIONIX_NAT_EXERCISE_ENDPOINT, headers=headers, json=parameters)
response.raise_for_status()
print(response.status_code, response.text)
