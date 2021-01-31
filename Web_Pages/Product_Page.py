from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from random import choice


class Product_Page(PageBase):

    def __init__(self):
        super().__init__()
        self.colors = self.get_elements(By.CSS_SELECTOR, '.productColor')
        self.name = self.get_element(By.XPATH, '//h1[@class="roboto-regular screen768 ng-binding"]').text
        self.color = ""
        self.quantity = ""

    def change_quantity(self, num):  # Change quantity of product
        self.get_element(By.CSS_SELECTOR, 'input[name="quantity"]').click()
        self.get_element(By.CSS_SELECTOR, 'input[name="quantity"]').send_keys(num)
        self.quantity = self.get_element(By.CSS_SELECTOR, 'input[name="quantity"]').get_attribute("value")

    def add_to_cart(self):  # Click on Add To Cart
        self.get_element(By.CSS_SELECTOR, 'button[name="save_to_cart"]').click()

    def choose_color(self):  # chooses product color
        x = self.get_element(By.CSS_SELECTOR, '.productColor')
        self.color = x.get_attribute("title")

    def buy_product(self, quantity):  # Do all buying action
        self.change_quantity(quantity)
        self.choose_color()
        self.add_to_cart()

    # a function that adds products to the cart, we use this a lot
    def add_product_to_cart(self, quantity):
        self.change_quantity(quantity)  # change product quantity
        self.add_to_cart()

    def get_product_name(self):
        return self.name

    def get_quantity(self):
        return self.get_element(By.CSS_SELECTOR, 'input[name="quantity"]').get_attribute("quantity")

    def get_price(self):  # slicing the $ sign off the price
        price = self.get_element(By.XPATH, '//h2[@class="roboto-thin screen768 ng-binding"]').text[1:].replace(',', '')
        return float(price)
