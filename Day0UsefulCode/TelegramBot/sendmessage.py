import requests
from auth import telegram_bot_token, telegram_bot_chat_ID


def send_message_to_telegram_bot(message):
    telegram_bot_url = "https://api.telegram.org/bot" + telegram_bot_token + "/sendMessage"
    telegram_parameters = {
        "chat_id": telegram_bot_chat_ID,
        "parse_mode": "Markdown",
        "text": message
    }
    telegram_response = requests.get(url=telegram_bot_url, params=telegram_parameters)
    telegram_response.raise_for_status()
    print(f"Telegram response: {telegram_response}")


send_message_to_telegram_bot("Sample Message")
