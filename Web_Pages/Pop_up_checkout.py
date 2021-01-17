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
        return self.get_element(By.XPATH, '//tr/td/span/label[@class="roboto-regular ng-binding"]')
