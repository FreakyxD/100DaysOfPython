import requests
from bs4 import BeautifulSoup
from sensitive import USER_AGENT
from submitdata import SubmitToGoogleSheets
from sensitive import GOOGLE_FORM_URL

ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(ZILLOW_CLONE_URL, headers=headers)
response.raise_for_status()

website_content = response.text

# Part 1 - Scrap the data

soup = BeautifulSoup(website_content, features="html.parser")

# apartment links
apartment_links_tags = soup.select(".property-card-link")

apartment_links = []
for apartment in apartment_links_tags:
    apartment_links.append(apartment["href"])

# apartment prices
apartment_prices_tags = soup.select(".PropertyCardWrapper__StyledPriceLine")

apartment_prices = []
for price in apartment_prices_tags:
    price = price.text

    if "+/mo" in price:
        price = price.replace("+/mo", "")
    elif "/mo" in price:
        price = price.replace("/mo", "")
    elif "+ 1 bd" in price:
        price = price.replace("+ 1 bd", "")
    elif "+ 1bd" in price:
        price = price.replace("+ 1bd", "")

    apartment_prices.append(price)

# apartment addresses
apartment_addresses_tags = soup.find_all("address")

apartment_addresses = []
for address in apartment_addresses_tags:
    address = address.text.strip()
    apartment_addresses.append(address)

apartments = {}
for n in range(len(apartment_links)):
    apartments[n] = {
        "Link": apartment_links[n],
        "Price": apartment_prices[n],
        "Address": apartment_addresses[n]
    }

# Part 2 - Submit the data
submitter = SubmitToGoogleSheets(GOOGLE_FORM_URL)
