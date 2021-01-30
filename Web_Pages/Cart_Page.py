from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase
import time

class Cart_Page(PageBase):

    def __init__(self):
        super().__init__()

    def get_price(self):
        # return self.get_element(By.ID, "checkOutButton")
        price = self.get_element(By.CSS_SELECTOR, 'table[class="fixedTableEdgeCompatibility"] \
                                                    span[class="roboto-medium ng-binding"]')
        return float(price.text[1:].replace(',', ''))  # deletes the $ and the comma, return a regular number

    def go_to_cart(self):
        self.get_element(By.ID, "menuCart").click()

    def get_page_path(self):  # checks if the page is indeed the shopping cart page
        time.sleep(2)
        return self.check_page_path(By.CSS_SELECTOR, "nav[class='pages fixedImportant'] a[class='select  ng-binding']")
        # return self.get_element(By.CSS_SELECTOR, "section.ng-scope > article > h3")

    def get_quantity_list(self): # get the list composed of product quantities in the cart page
        self.element_not_exist(By.XPATH, '//table[@class=""][@style=""]')
        rows = self.get_elements(By.CSS_SELECTOR, "table[CLASS='fixedTableEdgeCompatibility'] tr[class='ng-scope']")
        list_quantities = []
        for row in range(1, len(rows)+1):  # starting from the 1th row
            if row == (len(rows)+1):
                break
            list_quantities += [self.get_element(By.XPATH, f"//table/tbody/tr[{row}]/td[5]").text]
        return list_quantities

    def edit_quantity(self, row):  # edits the product quantity in a specific row in cart page summary table
        self.get_element(By.XPATH, f"//table/tbody/tr[{row}]/td[6]/span/a[@class='edit ng-scope']").click()
