from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Config.config import *
from Web_Pages.PageBase import PageBase
from selenium.webdriver.common.actions.pointer_actions import PointerActions


class Pop_up_checkout(PageBase):
    def __init__(self):
        super().__init__()
        # self.names = []
        # self.quantity = []
        # self.colors = []
        self.name = self.get_element(By.XPATH, '//h3[@class="ng-binding"]').text
        self.color = self.get_element(By.XPATH, '//tr/td/a/label/span').text
        self.quantity = self.get_element(By.XPATH, '//tr/td/a/label[1]').text.split(" ")[1]

    def get_total_quantity(self):
        return self.get_element(By.XPATH, '//tr/td/span/label[@class="roboto-regular ng-binding"]')

    def click_to_checkout(self):
        self.get_element(By.CSS_SELECTOR, '#checkOutPopUp').click()

    def get_quantity_after_purchase(self):
        self.get_element(By.ID, 'menuCart').click()
        return self.get_element(By.XPATH, '//label[@class="roboto-bold ng-scope"]').text







    # def get_names_of_all_products(self):
    #     list_names = []
    #     self.names = self.get_elements(By.XPATH, '//h3[@class="ng-binding"]')
    #     for i in range(len(self.names)):
    #         list_names += [self.names[i].text]
    #     self.names = list_names
    #
    # def get_quantity_of_all_products(self):
    #     list_quantity = []
    #     self.quantity = self.get_elements(By.XPATH, '//tr/td/a/label[1]')
    #     for i in range(len(self.quantity)):
    #         for letter in self.quantity[i].text:
    #             if letter.isdigit():
    #                 list_quantity += letter
    #     self.quantity = list_quantity
    #
    # def get_colors_of_all_products(self):
    #     list_colors = []
    #     self.colors = self.get_elements(By.XPATH, '//tr/td/a/label/span')
    #     for i in range(len(self.colors)):
    #         list_colors += [self.colors[i].text]
    #     self.colors = list_colors

