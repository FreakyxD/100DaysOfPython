from selenium import webdriver
from selenium.webdriver.common.by import By


class SubmitToGoogleSheets:
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.url = url
