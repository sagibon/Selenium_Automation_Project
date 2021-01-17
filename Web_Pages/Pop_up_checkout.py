from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Config.config import *


class Pop_up_checkout:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//tfoot/tr[1]/td/span/label[@class="roboto-regular ng-binding"]')))  # Waiting for the page to go up

    def get_quantity(self):
        return self.driver.find_element_by_xpath('//tfoot/tr[1]/td/span/label[@class="roboto-regular ng-binding"]').text
