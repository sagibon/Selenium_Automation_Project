import unittest
from Web_Pages.Main_Page import Main_Page
from Web_Pages.Category_Page import Category_Page
from Web_Pages.Product_Page import Product_Page
from Web_Pages.Pop_up_checkout import Pop_up_checkout
import time


class AOS_TESTS(unittest.TestCase):

    def setUp(self):
        Main_Page.get_main_page()
        self.main_page = Main_Page()

    def test_quantity_popup_checkout(self):
        self.main_page.click_on_category('tablets')
        self.category_page = Category_Page()         # click on the category page
        self.category_page.scan_products()  # get the list of the products that are in stock from the page
        self.category_page.click_on_product()
        self.product_page = Product_Page()
        self.product_page.change_quantity(3)  # change product quantity
        self.product_page.add_to_cart()

        self.pop_out = Pop_up_checkout()
        total = self.pop_out.get_total_quantity().text
        self.assertEqual(int(total), 3)



    def tearDown(self):
        time.sleep(5)
        # Main_Page.get_main_page()
        self.main_page.driver.quit()


if __name__ == '__main__':
    unittest.main()
