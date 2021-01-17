import unittest
from Web_Pages.Main_Page import Main_Page
from Web_Pages.Category_Page import Category_Page
from Web_Pages.Product_Page import Product_Page
import time


class AOS_TESTS(unittest.TestCase):

    def setUp(self):
        Main_Page.get_main_page()
        self.main_page = Main_Page()

    def test_quantity_popup_checkout(self):
        self.main_page.click_on_category('tablets')
        self.category_page = Category_Page()
        self.category_page.scan_products()
        self.category_page.click_on_product()
        Product_Page().change_quantity(5)

    def tearDown(self):
        time.sleep(5)
        # Main_Page.get_main_page()
        self.main_page.driver.quit()


if __name__ == '__main__':
    unittest.main()
