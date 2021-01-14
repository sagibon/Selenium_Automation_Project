from config import DRIVER_PATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Driver:

    def __init__(self):
        self.browser = webdriver.Firefox(executable_path=DRIVER_PATH)
        self.browser.implicitly_wait(5)
        self.browser.delete_all_cookies()
        self.browser.maximize_window()

    def wait_for_element(self, css_element):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_element)))




