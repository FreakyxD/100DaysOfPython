import requests
import datetime
from auth import NUTRITIONIX_APP_ID, NUTRITIONIX_API_KEY, SHEETY_BEARER_TOKEN
from sensitive import GENDER, WEIGHT_KG, HEIGHT_CM, AGE, SHEETY_PRIVATE_ENDPOINT

NUTRITIONIX_NAT_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


def get_nutritionix_data():
    nutritionix_response = requests.post(url=NUTRITIONIX_NAT_EXERCISE_ENDPOINT, headers=headers, json=parameters)
    nutritionix_response.raise_for_status()
    print(nutritionix_response.status_code)
    return nutritionix_response.json()


def format_nutritionix_data(filtered_exercise_dict):
    # extracts Date, Time, Exercise, Duration, Calories
    today_date = datetime.datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.datetime.now().strftime("%X")

    formatted_dictionary = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": filtered_exercise_dict["name"].title(),
            "duration": filtered_exercise_dict["duration_min"],
            "calories": filtered_exercise_dict["nf_calories"],
        }
    }
    return formatted_dictionary


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


all_exercise_list = get_nutritionix_data()["exercises"]

for exercise in all_exercise_list:
    formatted_exercise = format_nutritionix_data(exercise)
    sheety_response = requests.post(
        url=SHEETY_PRIVATE_ENDPOINT,
        json=formatted_exercise,
        auth=BearerAuth(SHEETY_BEARER_TOKEN)
    )
    sheety_response.raise_for_status()
    print("posting...\n", sheety_response.json())
