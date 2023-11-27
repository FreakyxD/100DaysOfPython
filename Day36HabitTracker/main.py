import requests
from auth import PIXELA_TOKEN
from sensitive import PIXELA_USERNAME

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Creating user - only once!
response = requests.post(url=pixela_endpoint, json=parameters)
print(response.text)
