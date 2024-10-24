import requests
from bs4 import BeautifulSoup
from Day0UsefulCode.TelegramBot.main import TelegramBot
from sensitive import USER_AGENT


def found_string_on_website(my_soup, search_string):
    return search_string.lower() in my_soup.get_text().lower()


telegram_bot = TelegramBot()

URL_TO_CHECK = "https://bitwarden.com/help/login-with-passkeys/"
STRING_TO_CHECK = "Log in with passkeys is currently in beta."  # not case-sensitive

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(URL_TO_CHECK, headers=headers)
response.raise_for_status()

website_source = response.text

soup = BeautifulSoup(website_source, "html.parser")

if not found_string_on_website(soup, STRING_TO_CHECK):
    print("Sending Telegram message...")
    telegram_bot.send_message_to_telegram_bot(f"Bitwarden Login with Passkeys is out of beta\n"
                                              f"More here: {URL_TO_CHECK}")
