from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://www.amazon.de/21249-Minecraft-Crafting-Building-Children/dp/B0BV7BC9X5")

price_euro = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_cent = driver.find_element(By.CLASS_NAME, "a-price-fraction")
price_symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol")
print(price_euro.text + "." + price_cent.text + price_symbol.text)

driver.quit()
