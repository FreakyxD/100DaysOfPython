from datetime import datetime, timezone
import requests
import time
from sensitive import MY_LAT, MY_LONG
from smtplib import SMTP
from auth import SMTP_SERVER, SMTP_SERVER_PORT, MY_EMAIL, MY_EMAIL_PASSWORD, TO_ADDRESS


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = data["iss_position"]["latitude"]
    iss_longitude = data["iss_position"]["longitude"]
    return iss_latitude, iss_longitude


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

    time_now = datetime.now(timezone.utc)
    hour_now = time_now.hour

    if sunrise <= hour_now <= sunset:
        return False
    else:
        return True


def is_iss_close():
    """Returns True if the ISS is within 5 degrees +/- of my current location"""
    coordinates = get_iss_position()
    iss_lat = float(coordinates[0])
    iss_lng = float(coordinates[1])

    lat_difference = iss_lat - MY_LAT
    lng_difference = iss_lng - MY_LONG

    if -5 <= lat_difference <= 5 and -5 <= lng_difference <= 5:
        return True
    else:
        return False


def send_mail():
    with SMTP(SMTP_SERVER, SMTP_SERVER_PORT) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_ADDRESS,
            msg="Subject: ISS is right above you\n\nLook up!"
        )


while True:
    if is_iss_close() and is_dark():
        send_mail()
    else:
        print("ISS is not visible above.")
    time.sleep(60)
