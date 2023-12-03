import requests
from auth import TELEGRAM_BOT_TOKEN, TELEGRAM_BOT_CHAT_ID

class TelegramBot:
    def __init__(self):
        self.TOKEN = TELEGRAM_BOT_TOKEN
        self.CHAT_ID = TELEGRAM_BOT_CHAT_ID
    def send_message_to_telegram_bot(self, message):
        telegram_bot_url = "https://api.telegram.org/bot" + self.TOKEN + "/sendMessage"
        telegram_parameters = {
            "chat_id": self.CHAT_ID,
            "parse_mode": "Markdown",
            "text": message
        }
        telegram_response = requests.get(url=telegram_bot_url, params=telegram_parameters)
        telegram_response.raise_for_status()
        print(f"Telegram response: {telegram_response}")
