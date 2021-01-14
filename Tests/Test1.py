import unittest
from Config.Driver import driver
from Web_Pages.Main_Page import Main_Page
from selenium import webdriver
import time
from Config.Driver import DRIVER_PATH


class AOS_TESTS(unittest.TestCase):

    def setUp(self):
        URL = "https://www.advantageonlineshopping.com/#/"
        self.driver = driver.get_driver().get(URL)
        self.main_page = Main_Page()

    def test_quantity_popup_checkout(self):
        self.main_page.click_on_category('tablets')
        time.sleep(5)

    def tearDown(self):
        self.main_page.driver.quit()


if __name__ == '__main__':
    unittest.main()
