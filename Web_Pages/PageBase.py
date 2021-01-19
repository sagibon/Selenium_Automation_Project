from Config.Driver import driver
from Config.config import TIMED_OUT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By


def element_not_exists(ltype, selector):
    WebDriverWait.until()


class PageBase:
    """Base class for all page objects in the Page Object Model"""

    def __init__(self):
        self.driver = driver.get_driver()
        self.driver.implicitly_wait(10)
        self._execute_with_wait(ec.invisibility_of_element_located((By.XPATH, '//div[@class="loader"]')))

    def _execute_with_wait(self, condition):
        return WebDriverWait(self.driver, 20).until(condition)

    def element_exists(self, ltype, selctors):
        try:
            self._execute_with_wait(
                ec.visibility_of_any_elements_located(
                    (ltype, selctors))
            )
            return True
        except TimeoutException:
            return False
        except ElementClickInterceptedException:
            pass
            self._execute_with_wait(
                ec.element_to_be_clickable(
                    (ltype, selctors))
            )
            return True

    def get_element(self, ltype,  selctors):
        if not self.element_exists(ltype, selctors):
            raise NoSuchElementException(f"Could not find {selctors}")
        return self.driver.find_element(ltype, selctors)

    def get_elements(self, ltype, selctors):
        if not self.element_exists(ltype, selctors):
            raise NoSuchElementException(f"Could not find {selctors}")
        return self.driver.find_elements(ltype, selctors)

    def element_not_exist(self, ltype, selectors):
        self._execute_with_wait(ec.invisibility_of_element_located((ltype, selectors)))

    def go_back(self):
        self.driver.execute_script("window.history.go(-1)")

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def get_current_url(self):
        return self.driver.current_url
