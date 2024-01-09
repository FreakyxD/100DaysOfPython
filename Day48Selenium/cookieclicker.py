import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

consent_btn = driver.find_element(By.CSS_SELECTOR, value=".fc-cta-consent > p:nth-child(2)")
consent_btn.click()

time.sleep(3)

language_select = driver.find_element(By.CSS_SELECTOR, value="#langSelect-EN")
language_select.click()

time.sleep(3)

cookie = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")


def buy_all_upgrades():
    while True:
        upgrades = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")

        if not upgrades:
            return
        print("Buying the highest upgrade")
        upgrades[-1].click()


def buy_highest_upgrade():
    upgrades = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")

    # check if any hits
    if upgrades:
        print("Buying the highest upgrade")
        upgrades[-1].click()

def buy_highest_upgrade_except_cursor():
    upgrades = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")

    # check if any hits
    if upgrades:
        if upgrades[-1].text != "Cursor\n15":
            print("Buying the highest upgrade")
            upgrades[-1].click()


def click_cookie():
    print("Clicking 🍪")
    cookie.click()


LOOP_STOP_MINUTES = 5
UPGRADE_FREQUENCY_SECONDS = 20

timeout = time.time() + 60 * LOOP_STOP_MINUTES
counter = time.time() + UPGRADE_FREQUENCY_SECONDS
while True:
    click_cookie()

    # every 5 seconds:
    if time.time() > counter:
        buy_highest_upgrade_except_cursor()

        # add another 5 seconds until the next check
        counter = time.time() + 5

    # after 5 minutes
    if time.time() > timeout:
        # print the final cookie per second count
        cookies_per_s = driver.find_element(By.CSS_SELECTOR, value="#cookiesPerSecond")
        print(cookies_per_s.text)
        break
