import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class InternetSpeedBot():
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.down = 0
        self.up = 0
        self.ping = 0
        self.units = {}
        self.url = url

    def test_internet_speed(self):
        self.driver.get(self.url)

        time.sleep(3)

        cookie_reject_btn = self.driver.find_element(By.ID, value="onetrust-reject-all-handler")
        cookie_reject_btn.click()

        start_btn = self.driver.find_element(By.CSS_SELECTOR, value=".start-text")
        print("Initiating Scan")
        start_btn.click()

        scan_in_progress = True

        while scan_in_progress:
            time.sleep(5)
            progress_check = self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed")
            if progress_check.get_attribute("data-upload-status-value") != "NaN":
                print("✅ Scan complete!")
                scan_in_progress = False
            else:
                print("⏳ Waiting for scan to finish.")

        time.sleep(3)

        thanks_btn = self.driver.find_element(By.CSS_SELECTOR, value="button.pure-button")
        thanks_btn.click()

        data_units = self.driver.find_elements(By.CSS_SELECTOR, value=".result-data-unit")
        self.units = {
            "download_unit": data_units[0].text,
            "upload_unit": data_units[1].text
        }

        # grab values
        self.down = float(self.driver.find_element(By.CSS_SELECTOR, value=".download-speed").text)
        self.up = float(self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed").text)
        self.ping = int(self.driver.find_element(By.CSS_SELECTOR, value=".ping-speed").text)

        self.driver.quit()

    def print_result(self):
        print(f"Download Speed: {self.down} {self.units['download_unit']}\nUpload Speed: {self.up} "
              f"{self.units['upload_unit']}\nPing: {self.ping}")


bot = InternetSpeedBot("https://www.speedtest.net")

bot.test_internet_speed()
bot.print_result()
