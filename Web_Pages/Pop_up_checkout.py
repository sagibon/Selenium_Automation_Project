from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Config.config import *
from Web_Pages.PageBase import PageBase


class Pop_up_checkout(PageBase):
    def __init__(self):
        super().__init__()

    def get_total_quantity(self):
        return self.get_element(By.CSS_SELECTOR, "a[id='shoppingCartLink']>span[class='cart ng-binding']")

    def remove_product(self):
        self.get_element(By.CSS_SELECTOR, "div[icon-x][class='removeProduct iconCss iconX']").click()
