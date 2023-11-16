from datetime import datetime
import requests
from Day33API_ISSTracker.locationdata import MY_LAT, MY_LONG


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iis_latitude = data["iss_position"]["latitude"]
    iis_longitude = data["iss_position"]["longitude"]
    return iis_latitude, iis_longitude


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    if sunrise <= hour_now <= sunset:
        return False
    else:
        return True


get_iss_position()
is_dark()
