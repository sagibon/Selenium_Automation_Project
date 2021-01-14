from random import choice
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Config import Driver


class Category_Page:

    def __init__(self):
        self.driver = Driver()
        self.driver.wait_for_element('.categoryTitle')  # Waiting for the page to go up
        self.products = self.driver.driver.find_elements_by_xpath(
            '//img[@class="imgProduct"]')  # Added products of this category which is in stock

    def click_on_product(self):  # Choose random product and click
        choice(self.products).click()
