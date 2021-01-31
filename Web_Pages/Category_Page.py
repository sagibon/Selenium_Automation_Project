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
    PRODUCTS = []

    def __init__(self):
        super().__init__()
        # self.products = []

    # scanning the products in stock only
    def scan_products(self):
        Category_Page.PRODUCTS = self.get_elements(By.XPATH, '//img[@class="imgProduct"]')

    def click_on_product(self):  # Choose random product and click
        time.sleep(3)
        self.element_not_exist(By.XPATH, '//h3[@class="roboto-regular center ng-scope"')
        self.element_not_exist(By.XPATH, '//div[@class="loader"]')
        choice(Category_Page.PRODUCTS).click()

    def scan_and_click(self):  # scans products and clicks on one of them
        self.scan_products()
        self.click_on_product()

