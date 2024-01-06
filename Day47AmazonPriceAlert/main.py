import requests
from bs4 import BeautifulSoup
from sensitive import USER_AGENT


product_url = input("Enter the URL to check: ")
buy_price = float(input("Enter the target price: "))
headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(product_url, headers=headers)
response.raise_for_status()

website_content = response.text

soup = BeautifulSoup(website_content, features="lxml")

price_tag = soup.select_one(".a-offscreen")
price = float(price_tag.text.strip("€").replace(",", "."))

print(f"Current price: {price}€")
if price <= buy_price:
    print("Buy now!")
else:
    print("Don't buy yet.")
