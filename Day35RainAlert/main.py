import requests
from Day33API_ISSTracker.locationdata import MY_LOCATION
from credentials import api_key

URL = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": MY_LOCATION[0],
    "lon": MY_LOCATION[1],
    "units": "metric",
    "appid": api_key,
}

# current https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# forecast https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
print(response)
