from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Product_Page:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Dolev\Desktop\Selenium\geckodriver.exe")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[name="save_to_cart"]')))  # Waiting for the page to go up

    def change_quantity(self, num):  # Change quantity of product
        self.driver.find_element_by_css_selector('input[name="quantity"]').send_keys(num)

    def add_to_cart(self):  # Click on Add To Cart
        self.driver.find_element_by_css_selector('button[name="save_to_cart"]').click()

    def get_quantity(self):
        return self.driver.find_element_by_css_selector('input[name="quantity"]').get_attribute("quantity")
