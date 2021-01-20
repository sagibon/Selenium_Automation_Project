from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase


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

    def get_page_path(self):  # checks the path in the left side of the page nav bar
        return self.check_page_path(By.CSS_SELECTOR, "nav[class='pages fixedImportant'] a[class='select  ng-binding']")

    def get_quantity_list(self): # get the list composed of product quantities in the cart page
        rows = self.get_elements(By.CSS_SELECTOR, "table[CLASS='fixedTableEdgeCompatibility'] tr[class='ng-scope']")
        list_quantities = []
        for row in range(1, len(rows)+1):  # starting from the 1th row
            if row == (len(rows)+1):
                break
            list_quantities += [self.get_element(By.XPATH, f"//table/tbody/tr[{row}]/td[5]").text]
        return list_quantities

    def edit_quantity(self, row):  # edits the product quantity in a specific row in cart page summary table
        self.get_element(By.XPATH, f"//table/tbody/tr[{row}]/td[6]/span/a[@class='edit ng-scope']").click()
