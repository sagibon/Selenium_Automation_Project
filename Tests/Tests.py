import unittest

from selenium.webdriver.common.keys import Keys

from Web_Pages.Main_Page import Main_Page
from Web_Pages.Category_Page import Category_Page
from Web_Pages.Product_Page import Product_Page
from Web_Pages.Pop_up_checkout import Pop_up_checkout
from Web_Pages.PageBase import PageBase
import time


class AOS_TESTS(unittest.TestCase):

    def add_product_to_cart(self, quantity):
        self.category_page.scan_products()  # get the list of the products that are in stock from the page
        self.category_page.click_on_product()
        self.product_page.change_quantity(quantity)  # change product quantity
        self.product_page.add_to_cart()
        self.product_page.go_back()

    def setUp(self):
        Main_Page.get_main_page()
        self.main_page = Main_Page()

    # test 1
    def test_1(self):
        self.main_page.click_on_category('tablets')
        self.category_page = Category_Page()         # click on the category page
        self.category_page.scan_and_click()
        self.product_page = Product_Page()
        self.add_product_to_cart(3)
        self.product_page.go_back()
        self.add_product_to_cart(2)

        # assertion - checking the total number of products in the cart
        self.pop_out = Pop_up_checkout()
        total = self.pop_out.get_total_quantity().text
        self.assertEqual(int(total), 5)

    # test 3
    def test_3(self):
        self.main_page.click_on_category('tablets')
        self.category_page = Category_Page()  # click on the category page
        self.category_page.scan_and_click()
        self.product_page = Product_Page()
        self.add_product_to_cart(3)
        self.product_page.go_back()
        self.add_product_to_cart(2)
        time.sleep(1)
        # removing a product from the popup cart
        self.pop_out = Pop_up_checkout()
        self.pop_out.remove_product()

        # assertion - checking the total number of products in the cart
        self.pop_out = Pop_up_checkout()
        total = self.pop_out.get_total_quantity().text
        self.assertNotEqual(int(total), 5)  # checks if only first products quantity left

    def tearDown(self):
        time.sleep(5)
        # Main_Page.get_main_page()
        self.main_page.driver.quit()


if __name__ == '__main__':
    unittest.main()






