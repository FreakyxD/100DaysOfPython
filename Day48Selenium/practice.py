from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.python.org/"

driver = webdriver.Firefox()
driver.get(url)
dates = driver.find_elements(By.CSS_SELECTOR, value="div.list-widgets.row > div.medium-widget.event-widget.last > div "
                                                    "> ul > li > time")
events = driver.find_elements(By.CSS_SELECTOR, value="div.list-widgets.row > div.medium-widget.event-widget.last > "
                                                     "div > ul > li > a")

# or a simple - for n in range(len(events)):
events_dict = {}
counter = 0
for date, event in zip(dates, events):
    events_dict.update(
        {
            counter: {
                "time": date.text,
                "name": event.text
            }
        }

    )
    counter += 1

pprint(events_dict)

driver.quit()
