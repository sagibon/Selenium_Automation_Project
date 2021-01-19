import unittest
from Web_Pages.Main_Page import Main_Page
from Web_Pages.Category_Page import Category_Page
from Web_Pages.Product_Page import Product_Page
from Web_Pages.Pop_up_checkout import Pop_up_checkout
from Web_Pages.OrderPaymentLogin_Page import OrderPaymentLogin
from Web_Pages.CreateAccount_Page import CreateAccount
from Web_Pages.PaymentMethod_Page import PaymentMethod_Page
from Web_Pages.Cart_Page import Cart_Page
from Web_Pages.PageBase import PageBase
import time


class AOS_TESTS(unittest.TestCase):

    def setUp(self):
        self.page_base = PageBase
        self.main_page = Main_Page()
        self.main_page.get_main_page()
        time.sleep(5)

    def test_quantity_popup_checkout(self):
        self.main_page.click_on_category('tablets')
        self.category_page = Category_Page()         # click on the category page
        self.category_page.scan_products()  # get the list of the products that are in stock from the page
        self.category_page.click_on_product()  # click_on_product
        self.product_page = Product_Page()
        self.product_page.change_quantity(3)  # change product quantity
        self.product_page.add_to_cart()  # add to cart
        self.product_page.go_back()  # go page back
        self.category_page.scan_products()  # scan for all products which is in stock
        self.category_page.click_on_product()  # click on product
        self.product_page.change_quantity(2)  # change quantity
        self.product_page.add_to_cart()  # add to cart
        self.pop_out = Pop_up_checkout()
        total = self.pop_out.get_total_quantity().text  # get quantity of the products together
        self.assertIn("5", total)  # Test

    def test_test2(self):
        self.main_page.click_on_category('tablets')  # click on category
        self.category_page = Category_Page()  # click on the category page
        self.category_page.scan_products()  # get the list of the products that are in stock from the page
        self.category_page.click_on_product()  # click on some product
        self.product_page1 = Product_Page()  # create instance
        self.product_page1.change_quantity(3)  # change product quantity
        self.product_page1.choose_color()  # choose color
        self.product_page1.add_to_cart()  # adding to cart
        p1 = [self.product_page1.name, self.product_page1.color, self.product_page1.quantity]  # Details of product 1
        self.p1_pop_up = Pop_up_checkout()
        p1_pop_up = [self.p1_pop_up.name, self.p1_pop_up.color, self.p1_pop_up.quantity]  # save PopUp details of product1
        self.main_page.get_main_page()  # back to main page
        self.main_page.click_on_category('mice')  # click on category
        self.category_page.scan_products()  # scan for all products which is in stock
        self.category_page.click_on_product()  # click on some product
        self.product_page2 = Product_Page()
        self.product_page2.change_quantity(5)  # change product quantity
        self.product_page2.choose_color()  # choose color
        self.product_page2.add_to_cart()  # add to cart
        p2 = [self.product_page2.name, self.product_page2.color, self.product_page2.quantity]  # Details of product 2
        self.p2_pop_up = Pop_up_checkout()
        p2_pop_up = [self.p2_pop_up.name, self.p2_pop_up.color, self.p2_pop_up.quantity] # save PopUp details of product2
        self.main_page.get_main_page()
        self.main_page.click_on_category('headphones')  # click on category
        self.category_page.scan_products()  # scan for all products which is in stock
        self.category_page.click_on_product()  # click on some product
        self.product_page3 = Product_Page()
        self.product_page3.change_quantity(8)  # change quantity
        self.product_page3.choose_color()  # choose some color
        self.product_page3.add_to_cart()  # add to cart
        self.pop_up_checkout = Pop_up_checkout()
        p3 = [self.product_page3.name, self.product_page3.color, self.product_page3.quantity] # Details of product 3
        self.p3_pop_up = Pop_up_checkout()
        p3_pop_up = [self.p3_pop_up.name, self.p3_pop_up.color, self.p3_pop_up.quantity]  # save PopUp details of product3
        self.assertEqual(p1, p1_pop_up)  # Test1
        self.assertEqual(p2, p2_pop_up)  # Test2
        self.assertEqual(p3, p3_pop_up)  # Test3

    def test_tet7(self):
        main_page_url = self.main_page.get_current_url()  # get main page URL
        self.main_page.click_on_category('tablets')  # click on the category page
        self.category_page = Category_Page()
        tablet_url = self.main_page.get_current_url()  # get current URL
        self.category_page.scan_products()  # get the list of the products that are in stock from the page
        self.category_page.click_on_product()  # click on some product
        self.product_page = Product_Page()  # create instance
        self.product_page.add_to_cart()  # adding to cart
        self.main_page.go_back()  # go page back
        current_url = self.main_page.get_current_url() # get current URL after back page
        self.assertEqual(tablet_url, current_url)  # Test URL
        self.main_page.go_back()  # go page back
        check_main_page_url = self.main_page.get_current_url()  # save current URL
        self.assertEqual(main_page_url, check_main_page_url)  # Test URL

    def test_test8(self):
        self.main_page.click_on_category('tablets')
        self.category_page = Category_Page()  # click on the category page
        self.category_page.scan_products()  # get the list of the products that are in stock from the page
        self.category_page.click_on_product()  # click on some product
        self.product_page1 = Product_Page()  # create instance
        self.product_page1.add_to_cart()  # adding to cart
        product_name = self.product_page1.name  # save product name
        self.pop_up_checkout = Pop_up_checkout()
        self.pop_up_checkout.click_to_checkout()  # click to checkout
        self.order_payment_login = OrderPaymentLogin()
        self.order_payment_login.click_to_register()  # click to register to continue payment process
        self.create_account = CreateAccount()
        self.create_account.enter_valid_details()  # enter valid details
        self.order_payment_login.click_next()  # confirm shipping details by click Next
        self.payment_method = PaymentMethod_Page()
        self.payment_method.pay_with_safepay()  # pay with SafePay
        self.assertEqual("Thank you for buying with Advantage", self.payment_method.thank_you())
        check_empty = self.pop_up_checkout.get_quantity_after_purchase()
        self.assertIn("Your shopping cart is empty", check_empty)
        x = Cart_Page().check_user_orders()
        self.assertEqual(product_name, x.upper())
    def test_test9(self):

        self.main_page.click_on_category('tablets')
        self.category_page = Category_Page()  # click on the category page
        self.category_page.scan_products()  # get the list of the products that are in stock from the page
        self.category_page.click_on_product()  # click on some product
        self.product_page1 = Product_Page()  # create instance
        self.product_page1.add_to_cart()  # adding to cart
        product_name = self.product_page1.name  # save product name
        self.pop_up_checkout = Pop_up_checkout()
        self.pop_up_checkout.click_to_checkout()  # click to checkout
        self.order_payment_login = OrderPaymentLogin()
        self.order_payment_login.login_with_exist_user('test_xyz', 'Aasd123')  # enter exist user
        self.order_payment_login.click_next()  # click next to verify shipping details
        self.payment_method = PaymentMethod_Page()
        self.payment_method.pay_with_mastercredit()  # pay with MasterCredit
        self.assertEqual("Thank you for buying with Advantage", self.payment_method.thank_you())  # Test payment
        check_empty = self.pop_up_checkout.get_quantity_after_purchase()
        self.assertIn("Your shopping cart is empty", check_empty)  # check shopping cart is empty
        x = Cart_Page().check_user_orders()
        self.assertEqual(product_name, x.upper())  # check product in order list


    def tearDown(self):
        time.sleep(2)
        self.main_page.close()


if __name__ == '__main__':
    unittest.main()
