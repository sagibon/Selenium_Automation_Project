import unittest
from Web_Pages.Main_Page import Main_Page
from Web_Pages.Category_Page import Category_Page
from Web_Pages.Product_Page import Product_Page
from Web_Pages.Pop_up_checkout import Pop_up_checkout
import time
from Web_Pages.PageBase import PageBase


class AOS_TESTS(unittest.TestCase):

    def setUp(self):
        # Main_Page.get_main_page()
        self.main_page = Main_Page()
        time.sleep(5)
        self.main_page.driver.maximize_window()

        # self.page_base = PageBase()
        # self.main_page = Main_Page()
        # self.main_page.get_main_page()
        # time.sleep(5)

    def test_quantity_popup_checkout(self):
        self.main_page.click_on_category('tablets')
        self.category_page = Category_Page()         # click on the category page
        self.category_page.scan_products()  # get the list of the products that are in stock from the page
        self.category_page.click_on_product()
        self.product_page = Product_Page()
        self.product_page.change_quantity(3)  # change product quantity
        self.product_page.add_to_cart()
        self.product_page.go_back()
        self.category_page.scan_products()
        self.category_page.click_on_product()
        self.product_page.change_quantity(2)
        self.product_page.add_to_cart()
        self.pop_out = Pop_up_checkout()
        total = self.pop_out.get_total_quantity().text
        self.assertIn("5", total)

    # def test_test2(self):
    #     self.main_page.click_on_category('tablets')
    #     self.category_page = Category_Page()  # click on the category page
    #     self.category_page.scan_products()  # get the list of the products that are in stock from the page
    #     self.category_page.click_on_product()  # click on some product
    #     self.product_page1 = Product_Page()  # create instance
    #     self.product_page1.change_quantity(3)  # change product quantity
    #     self.product_page1.choose_color()  # choose color
    #     self.product_page1.add_to_cart()  # adding to cart
    #     p1 = [self.product_page1.name, self.product_page1.color, self.product_page1.quantity]  # save product parameters
    #     self.p1_pop_up = Pop_up_checkout()
    #     p1_pop_up = [self.p1_pop_up.name, self.p1_pop_up.color, self.p1_pop_up.quantity]  # save pop_up parameters of this product
    #     self.main_page.get_main_page()  # back to main page
    #     self.main_page.click_on_category('mice')
    #     self.category_page.scan_products()  # get the list of the products that are in stock from the page
    #     self.category_page.click_on_product()
    #     self.product_page2 = Product_Page()
    #     self.product_page2.change_quantity(5)  # change product quantity
    #     self.product_page2.choose_color()
    #     self.product_page2.add_to_cart()
    #     p2 = [self.product_page2.name, self.product_page2.color, self.product_page2.quantity]
    #     self.p2_pop_up = Pop_up_checkout()
    #     p2_pop_up = [self.p2_pop_up.name, self.p2_pop_up.color, self.p2_pop_up.quantity]
    #     self.main_page.get_main_page()
    #     self.main_page.click_on_category('headphones')
    #     self.category_page.scan_products()
    #     self.category_page.click_on_product()
    #     self.product_page3 = Product_Page()
    #     self.product_page3.change_quantity(8)
    #     self.product_page3.choose_color()
    #     self.product_page3.add_to_cart()
    #     self.pop_up_checkout = Pop_up_checkout()
    #     p3 = [self.product_page3.name, self.product_page3.color, self.product_page3.quantity]
    #     self.p3_pop_up = Pop_up_checkout()
    #     p3_pop_up = [self.p3_pop_up.name, self.p3_pop_up.color, self.p3_pop_up.quantity]
    #     self.assertEqual(p1, p1_pop_up)
    #     self.assertEqual(p2, p2_pop_up)
    #     self.assertEqual(p3, p3_pop_up)

    # def test_tet7(self):
    #     main_page_url = self.page_base.get_current_url()  # get main page URL
    #     self.main_page.click_on_category('tablets')
    #     self.category_page = Category_Page()  # click on the category page
    #     tablet_url = self.page_base.get_current_url()  # get current URL
    #     self.category_page.scan_products()  # get the list of the products that are in stock from the page
    #     self.category_page.click_on_product()  # click on some product
    #     self.product_page = Product_Page()  # create instance
    #     self.product_page.add_to_cart()  # adding to cart
    #     self.page_base.go_back()  # go page back
    #     current_url = self.page_base.get_current_url() # get current URL after back page
    #     self.assertEqual(tablet_url, current_url)
    #     self.page_base.go_back()
    #     check_main_page_url = self.page_base.get_current_url()
    #     self.assertEqual(main_page_url, check_main_page_url)

    def tearDown(self):
        time.sleep(5)
        self.main_page.close()


if __name__ == '__main__':
    unittest.main()
