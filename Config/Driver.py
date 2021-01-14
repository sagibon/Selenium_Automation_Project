from config import DRIVER_PATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Driver(object):
    """Singleton class for interacting with the selenium webdriver object"""
    instance = None

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=DRIVER_PATH)

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()
        instance = None

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)

driver = Driver.get_instance()


'''
class Driver:



    def __init__(self):
        global driver
        self.driver = webdriver.Firefox(executable_path=DRIVER_PATH)
        self.driver.implicitly_wait(5)
        # self.driver.get('https://www.advantageonlineshopping.com/#/')
        # self.driver.implicitly_wait(5)
        # self.driver.delete_all_cookies()
        # self.driver.maximize_window()

    # def go_to_main_page(self):


    def wait_for_element(self, css_element):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_element)))
'''



