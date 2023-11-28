import requests
from datetime import datetime
from auth import PIXELA_TOKEN
from sensitive import PIXELA_USERNAME, PIXELA_GRAPH_ID, PIXELA_TIMEZONE

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
graph_endpoint_id = graph_endpoint + f"/{PIXELA_GRAPH_ID}"

parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Creating user - only once!
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)


graph_config = {
    "id": PIXELA_GRAPH_ID,
    "name": "100 Days of Python",
    "unit": "hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

# Creating graph - only once!
# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
# print(response.text)


# Changing graph
# graph_config_changes = {
#     "timezone": PIXELA_TIMEZONE
# }
# response = requests.post(url=graph_endpoint_id, headers=headers, json=graph_config_changes)
# print(response)

# Post a Pixel
current_date = datetime.now()
formatted_date = current_date.strftime("%Y%m%d")

pixel_config = {
    "date": formatted_date,
    "quantity": "1"
}
request = requests.post(url=graph_endpoint_id, headers=headers, json=pixel_config)
print(request)
