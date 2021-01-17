from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase
from selenium.webdriver.common.keys import Keys


class Product_Page(PageBase):

    def __init__(self):
        super().__init__()

    def change_quantity(self, num):  # Change quantity of product
        self.get_element(By.CSS_SELECTOR, 'input[name="quantity"]').send_keys(Keys.BACK_SPACE)

    def add_to_cart(self):  # Click on Add To Cart
        self.get_element(By.CSS_SELECTOR, 'button[name="save_to_cart"]').click()

    def get_quantity(self):
        return self.get_element(By.CSS_SELECTOR, 'input[name="quantity"]').get_attribute("quantity")
