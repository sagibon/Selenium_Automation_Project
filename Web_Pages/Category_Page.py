import time
from random import choice
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Config import Driver
from Web_Pages.PageBase import PageBase
from Config.Driver import driver
import time


class Category_Page(PageBase):

    def __init__(self):
        super().__init__()
        self.products = []

    # scanning the products in stock only
    def scan_products(self):
        self.products = self.get_elements(By.XPATH, '//img[@class="imgProduct"]')

    def click_on_product(self):  # Choose random product and click
        self.element_not_exist(By.XPATH, '//div[@class="loader"]')
        choice(self.products).click()

    def scan_and_click(self):
        self.scan_products()
        self.click_on_product()
