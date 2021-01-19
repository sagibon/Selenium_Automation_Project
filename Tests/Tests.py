import unittest
from selenium.webdriver.common.keys import Keys
from Web_Pages.Main_Page import Main_Page
from Web_Pages.Category_Page import Category_Page
from Web_Pages.Product_Page import Product_Page
from Web_Pages.Pop_up_checkout import Pop_up_checkout
from Web_Pages.Cart_Page import Cart_Page
from Web_Pages.PageBase import PageBase
import time


class AOS_TESTS(unittest.TestCase):
    # a function that adds products to the cart, we use this a lot
    def add_product_to_cart(self, quantity):
        self.category_page.scan_products()  # get the list of the products that are in stock from the page
        self.category_page.click_on_product()
        time.sleep(1)
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

    def test_4(self):
        # making an order:
        self.main_page.click_on_category('speakers')
        self.category_page = Category_Page()
        self.category_page.scan_and_click()
        self.product_page = Product_Page()
        self.add_product_to_cart(5)
        self.cart_page = Cart_Page()
        self.cart_page.go_to_cart()  # go to cart page
        location = self.cart_page.get_page_path().text  # checks page path
        print(location, " is SHOPPING CART PAGE")
        self.assertIn("SHOPPING CART", location)

    def test_5(self):
        self.main_page.click_on_category('tablets')
        self.category_page = Category_Page()  # click on the category page
        self.category_page.scan_and_click()
        self.product_page = Product_Page()
        self.add_product_to_cart(3)
        self.product_page.go_back()
        self.add_product_to_cart(2)
        # go to cart page
        self.cart_page = Cart_Page()
        self.pop_out = Pop_up_checkout()
        self.cart_page.go_to_cart()
        price = self.cart_page.get_price().text  # get total cart price
        price2 = self.pop_out.get_total_price().text  # get pop-out cart price
        # compare pop-out cart total price to cart page total price
        print(price + " vs " + price2)
        self.assertEqual(price, price2)

    def test_6(self):
        self.main_page.click_on_category('headphones')
        self.category_page = Category_Page()  # click on the category page
        self.category_page.scan_and_click()
        self.product_page = Product_Page()
        self.add_product_to_cart(3)
        self.product_page.go_back()
        self.add_product_to_cart(2)
        # go to cart page
        self.cart_page = Cart_Page()
        self.cart_page.go_to_cart()
        # get the list of current quantities on page
        list1 = self.cart_page.get_quantity_list()  # list of the first  2 product quantities
        print(list1)
        self.cart_page.edit_quantity(1)  # goes to edit the products in the first row
        self.product_page.change_quantity(4)
        self.product_page.add_to_cart()
        self.cart_page.go_to_cart()  # navigates to cart page
        # change the second product quantity
        self.cart_page.edit_quantity(2)
        self.product_page.change_quantity(5)
        self.product_page.add_to_cart()
        # go to cart page
        self.cart_page.go_to_cart()
        list2 = self.cart_page.get_quantity_list() # list of the new product quantities
        print(list2)
        self.assertNotEqualEqual(list1, list2)  # comparing both products

    def test_10(self):
        pass

    def tearDown(self):
        time.sleep(3)
        # Main_Page.get_main_page()
        self.main_page.driver.quit()


if __name__ == '__main__':
    unittest.main()






