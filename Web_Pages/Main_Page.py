from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Config.Driver import driver
from Config.Driver import DRIVER_PATH

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class PageBase:
    """Base class for all page objects in the Page Object Model"""

    def __init__(self):
        self.driver = driver.get_driver()

    def _execute_with_wait(self, condition):
        return WebDriverWait(self.driver, 5).until(condition)

    def element_exists(self, ltype, selctors):
        try:
            self._execute_with_wait(
                ec.presence_of_element_located(
                    ( ltype, selctors))
            )
            return True
        except TimeoutException:
            return False

    def get_element(self, ltype, selctors):
        if not self.element_exists(ltype, selctors):
            raise NoSuchElementException("Could not find {locator.selector}")
        return self.driver.find_element(ltype, selctors)




class Main_Page(PageBase):


    categories = {"headphones": "#headphonesImg", "mice": "#miceImg", "laptops": "#laptopsImg",
                       "speakers": "#speakersImg", "tablets": "#tabletsImg"}


    def __init__(self):
        super().__init__()

    def click_on_category(self, category):
        #self.driver.find_element_by_css_selector(self.categories[category_name]).click()
        Cat = self.get_element(By.CSS_SELECTOR,self.categories[category])
        Cat.click()
