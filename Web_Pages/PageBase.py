from Config.Driver import driver
from Config.config import TIMED_OUT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By


class PageBase:
    """Base class for all page objects in the Page Object Model"""

    def __init__(self):
        self.driver = driver.get_driver()
        self._execute_with_wait(ec.invisibility_of_element_located((By.XPATH, '//div[@class="loader"]')))

    def _execute_with_wait(self, condition):
        return WebDriverWait(self.driver, TIMED_OUT).until(condition)

    def element_exists(self, ltype, selctors):
        try:
            self._execute_with_wait(
                ec.visibility_of_element_located(
                    (ltype, selctors))
            )
            return True
        except TimeoutException:
            return False

    def get_element(self, ltype,  selctors):
        if not self.element_exists(ltype, selctors):
            raise NoSuchElementException(f"Could not find {selctors}")
        return self.driver.find_element(ltype, selctors)

    def get_elements(self, ltype, selctors):
        if not self.element_exists(ltype, selctors):
            raise NoSuchElementException(f"Could not find {selctors}")
        return self.driver.find_elements(ltype, selctors)
