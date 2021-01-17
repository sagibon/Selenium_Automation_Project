from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase


class Cart_Page(PageBase):

    def __init__(self):
        super().__init__()

    def get_price(self):
        return self.get_element(By.ID, "checkOutButton")

    def go_to_cart(self):
        self.get_element(By.ID, "menuCart").click()