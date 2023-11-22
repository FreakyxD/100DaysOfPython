import pprint
import requests
from sensitive import MY_LAT, MY_LONG
from datetime import datetime

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}

# API request
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]  # 2023-11-16T16:23:09+00:00

print("API Response:")
pprint.pprint(data)

print(f"sunrise: {sunrise}")
print(f"sunset: {sunset}")

time_now = datetime.now()

date_today = time_now.date()
hour_now = time_now.hour
print(date_today)
print(f"hour: {hour_now}")

# comparing API response with actual hour
sunset_hour = int(sunset.split("T")[1].split(":")[0])
if sunset_hour == hour_now:
    print("Sunset hour")
else:
    print("No sunset hour")
