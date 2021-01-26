from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Config.config import *
from Web_Pages.PageBase import PageBase
from selenium.webdriver.common.actions.pointer_actions import PointerActions


class Pop_up_checkout(PageBase):
    def __init__(self):
        super().__init__()
        try:
            self.name = self.get_element(By.XPATH, '//h3[@class="ng-binding"]').text
            self.color = self.get_element(By.XPATH, '//tr/td/a/label/span').text
            self.quantity = self.get_element(By.XPATH, '//tr/td/a/label[1]').text.split(" ")[1]

        except:
            pass

    def get_total_quantity(self):
        try:  # if all products deleted, return the total above the cart icon which will be zero:
            return self.get_element(By.XPATH, '//tr/td/span/label[@class="roboto-regular ng-binding"]')

        except NoSuchElementException:
            return self.get_element(By.CSS_SELECTOR, 'span[class="cart ng-binding"]')

    def click_to_checkout(self):
        self.get_element(By.CSS_SELECTOR, '#checkOutPopUp').click()

    def get_quantity_after_purchase(self):
        self.get_element(By.ID, 'menuCart').click()
        return self.get_element(By.XPATH, '//label[@class="roboto-bold ng-scope"]').text

    def remove_product(self):
        self.get_element(By.CSS_SELECTOR, "div[icon-x][class='removeProduct iconCss iconX']").click()

    def get_total_price(self):
        return self.get_element(By.ID, "checkOutPopUp")