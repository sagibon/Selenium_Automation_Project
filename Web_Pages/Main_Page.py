from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Main_Page:

    url = 'https://www.advantageonlineshopping.com/#/'

    def __init__(self, driver):
        self.driver = driver
        self.categories = {"headphones": "#headphonesImg", "mice": "#miceImg", "laptops": "#laptopsImg",
                           "speakers": "#speakersImg", "tablets": "tabletsImg"}
        # self.wait_for_element("html")

    def load(self):
        self.driver.get(self.url)

    def click_on_category(self, category_name):
        self.driver.find_element_by_css_selector(self.categories[category_name]).click()





