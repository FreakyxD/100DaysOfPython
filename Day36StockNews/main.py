import requests
from auth import ALPHA_VANTAGE_API_KEY as STOCK_API, NEWS_API_KEY
from Day0UsefulCode.TelegramBot.main import TelegramBot
# from sampledata import sample_stock_data as stock_data - Sample data if API is limiting requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NUMBER_OF_ARTICLES = 3


def changed_5_percent(yesterday_price, day_before_price):
    delta_percent = (yesterday_price - day_before_price) * 100 / day_before_price
    if delta_percent <= -5 or delta_percent >= 5:
        return round(delta_percent)


def format_send(percent_change, news_list):
    titles = [news["title"] for news in news_list[:NUMBER_OF_ARTICLES]]
    descriptions = [news["description"] for news in news_list[:NUMBER_OF_ARTICLES]]
    urls = [news["url"] for news in news_list[:NUMBER_OF_ARTICLES]]

    # prepare symbol and percentage number
    if percent_change < 0:
        # decrease
        symbol = "🔻"
        percent_change = abs(percent_change)
    else:
        # increase
        symbol = "🔺"

    for title, description, url in zip(titles, descriptions, urls):
        message = f"{STOCK}: {symbol}{percent_change}%\nHeadline: {title}\nLink: {description}\nURL: {url}"
        telegram_bot = TelegramBot()
        telegram_bot.send_message_to_telegram_bot(message)


stock_endpoint = "https://www.alphavantage.co/query?"
parameter = {
    "apikey": STOCK_API,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
}
response = requests.get(url=stock_endpoint, params=parameter)
response.raise_for_status()
stock_data = response.json()


data_previous_days = [value for (key, value) in stock_data["Time Series (Daily)"].items()]
last_close_price = round(float(data_previous_days[0]["4. close"]), 2)
day_before_last_close_price = round(float(data_previous_days[1]["4. close"]), 2)

percent = changed_5_percent(last_close_price, day_before_last_close_price)
if percent:
    news_endpoint = "https://newsapi.org/v2/everything"
    parameter = {
        "apiKey": NEWS_API_KEY,
        "pageSize": NUMBER_OF_ARTICLES,
        "qInTitle": COMPANY_NAME,
    }
    response = requests.get(url=news_endpoint, params=parameter)
    response.raise_for_status()
    news_data = response.json()
    article_data = news_data["articles"]
    format_send(percent, article_data)
