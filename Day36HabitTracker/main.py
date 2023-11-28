import requests
from datetime import datetime
from auth import PIXELA_TOKEN
from sensitive import PIXELA_USERNAME, PIXELA_GRAPH_ID, PIXELA_TIMEZONE

current_date = datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
graph_endpoint_id = graph_endpoint + f"/{PIXELA_GRAPH_ID}"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

user_creation_parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": PIXELA_GRAPH_ID,
    "name": "100 Days of Python",
    "unit": "hours",
    "type": "float",
    "color": "sora",
}


# Creating user - only once!
def create_user():
    response = requests.post(url=pixela_endpoint, json=user_creation_parameters)
    print(response, response.text)


# Creating graph - only once!
def create_graph():
    response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
    print(response.text)


# Changing graph
def change_graph_config():
    graph_config_changes = {
        "timezone": PIXELA_TIMEZONE
    }
    response = requests.put(url=graph_endpoint_id, headers=headers, json=graph_config_changes)
    print(response, response.text)


def post_a_pixel(amount):
    pixel_config = {
        "date": current_date,
        "quantity": str(amount)
    }
    response = requests.post(url=graph_endpoint_id, headers=headers, json=pixel_config)
    return response, response.text


def update_a_pixel(amount):
    put_endpoint = graph_endpoint_id + f"/{current_date}"
    update_config = {
        "quantity": str(amount),
    }

    response = requests.put(url=put_endpoint, headers=headers, json=update_config)
    print(response, response.text)


def delete_a_pixel():
    delete_endpoint = graph_endpoint_id + f"/{current_date}"

    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response, response.text)
