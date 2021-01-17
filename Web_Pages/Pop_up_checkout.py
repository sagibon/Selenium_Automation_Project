from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Config.config import *
from Web_Pages.PageBase import PageBase


class Pop_up_checkout(PageBase):
    def __init__(self):
        super().__init__()
        self.names = []

    def get_total_quantity(self):
        return self.get_element(By.XPATH, '//tr/td/span/label[@class="roboto-regular ng-binding"]')

    def get_names_of_all_products(self):
        list_names = []
        self.names = self.get_elements(By.XPATH, '//h3[@class="ng-binding"]')
        for product_name in range(len(self.names)):
            list_names += [self.names[product_name].text]
        return list_names

    def get_quantity_of_all_products(self):
        list_quantity = []
        self.quantity = self.get_elements(By.XPATH, '//tr/td/a/label[1]')
        for quantity in range(len(self.quantity)):
            list_quantity += [self.quantity[quantity].text]
        return list_quantity

    def get_colors_of_all_products(self):
        list_colors = []
        self.colors = self.get_elements(By.XPATH, '//tr/td/a/label/span')
        for colors in range(len(self.colors)):
            list_colors += [self.colors[colors].text]



