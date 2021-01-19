import unittest
from pyexpat import features

import behave

from Web_Pages.Main_Page import Main_Page
from Web_Pages.Category_Page import Category_Page
from Web_Pages.Product_Page import Product_Page
from Web_Pages.Pop_up_checkout import Pop_up_checkout
import time
from Web_Pages.PageBase import PageBase
import behave


class AOS_TESTS(unittest.TestCase):
    def setUp(self):
        # Main_Page.get_main_page()
        self.main_page = Main_Page()
        time.sleep(5)
        self.main_page.driver.maximize_window()

    def tearDown(self):
        time.sleep(5)
        self.main_page.close()


if __name__ == '__main__':
    unittest.main()
