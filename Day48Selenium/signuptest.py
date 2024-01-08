from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
sign_up_btn = driver.find_element(By.CLASS_NAME, value="btn.btn-lg.btn-primary.btn-block")

first_name.send_keys("Max")
last_name.send_keys("Mustermann")
email.send_keys("max.mustermann@gmail.com")
sign_up_btn.click()

driver.quit()
