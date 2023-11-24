import requests
from sensitive import MY_LOCATION
from auth import OWM_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_BOT_CHAT_ID


# current https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# forecast https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

def send_message_to_telegram_bot(message):
    telegram_bot_url = "https://api.telegram.org/bot" + TELEGRAM_BOT_TOKEN + "/sendMessage"
    telegram_parameters = {
        "chat_id": TELEGRAM_BOT_CHAT_ID,
        "parse_mode": "Markdown",
        "text": message
    }
    telegram_response = requests.get(url=telegram_bot_url, params=telegram_parameters)
    telegram_response.raise_for_status()
    print(f"Telegram response: {telegram_response}")


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
    send_message_to_telegram_bot("It's going to rain today. Remember to bring an ☔️")
