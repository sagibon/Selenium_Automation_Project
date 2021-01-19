from Config.config import DRIVER_PATH
from selenium import webdriver


class Driver(object):
    """Singleton class for interacting with the selenium webdriver object"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
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

