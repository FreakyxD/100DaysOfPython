from datetime import datetime
import requests
from Day33API_ISSTracker.locationdata import MY_LAT, MY_LONG
from smtplib import SMTP
from Day32EmailSMTP.credentials import SMTP_SERVER, SMTP_SERVER_PORT, MY_EMAIL, MY_PASSWORD, TO_ADDRESS


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


def is_iis_close():
    """Returns True if the ISS is within 5 degrees +/- of my current location"""
    # TODO each lat and lng need to be +-5 of current lat and long
    # then, return true
    coordinates = get_iss_position()
    iis_lat = coordinates[0]
    iis_lng = coordinates[1]

    lat_difference = iis_lat - MY_LAT
    lng_difference = iis_lng - MY_LONG

    if -5 <= lat_difference <= 5 and -5 <= lng_difference <= 5:
        print("within +-5")
        return True
    else:
        print("not close")
        return False


def send_mail():
    # debug
    if True:
        print("Subject: IIS is right above you\n\nLook up!")
        return
    with SMTP(SMTP_SERVER, SMTP_SERVER_PORT) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_ADDRESS,
            msg="Subject: IIS is right above you\n\nLook up!"
        )


# if is_iis_close() and is_dark() --> send mail to look up
is_iis_close()
is_dark()
