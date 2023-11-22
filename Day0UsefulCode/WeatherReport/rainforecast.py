import requests
from auth import OWM_API_KEY
from sensitive import MY_LOCATION


# current https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# forecast https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}


URL = "https://api.openweathermap.org/data/2.8/onecall"
parameters = {
    "lat": MY_LOCATION["latitude"],
    "lon": MY_LOCATION["longitude"],
    "units": "metric",
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()
print(f"Response code: {response.status_code}")

# If weather code ID < 700 -> bring umbrella
hourly_forecast = data["hourly"]

need_umbrella = False
for hour in hourly_forecast[:12]:  # iterate through the next 11 hours
    for weather in hour["weather"]:  # iterate through all weather conditions
        if weather["id"] < 700:
            need_umbrella = True
            break
    if need_umbrella:
        break

if need_umbrella:
    print("It's going to rain today. Remember to bring an ☔️")
