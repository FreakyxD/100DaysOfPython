from selenium import webdriver
from selenium.webdriver.common.by import By


class SubmitToGoogleSheets:
    def __init__(self, url, apartment_listings):
        self.driver = webdriver.Firefox()
        self.url = url
        self.apartment_listings = apartment_listings

        # load website
        self.driver.get(url)

    def submit_data(self):
        for apartment in self.apartment_listings.values():
            self.driver.implicitly_wait(3)

            # define html objects
            input_fields = self.driver.find_elements(By.CSS_SELECTOR, value=".whsOnd.zHQkBf")
            address_input = input_fields[0]
            price_input = input_fields[1]
            link_input = input_fields[2]

            submit_btn = self.driver.find_element(By.XPATH,
                                                  value="/html/body/div/div[2]/form/div[2]/div/div[3]/div["
                                                        "1]/div[1]/div")

            self.driver.implicitly_wait(3)

            # clicking on first input to prevent error
            address_input.click()

            print("Filling form...")

            # address
            address_input.send_keys(apartment["Address"])

            # price
            price_input.send_keys(apartment["Price"])

            # link
            link_input.send_keys(apartment["Link"])

            print("Submitting Data ✅")

            # submit
            submit_btn.click()

            self.driver.implicitly_wait(3)

            # finding the repeat button
            new_response_lnk = self.driver.find_element(By.XPATH,
                                                        value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            new_response_lnk.click()

        self.driver.quit()
