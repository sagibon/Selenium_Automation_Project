from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase


class Cart_Page(PageBase):

    def __init__(self):
        super().__init__()

    def get_price(self):
        return self.get_element(By.ID, "checkOutButton")

    def go_to_cart(self):
        self.get_element(By.ID, "menuCart").click()

    def get_page_path(self): # checks the path in the left side of the page nav bar
        return self.check_page_path(By.CSS_SELECTOR, "nav[class='pages fixedImportant'] a[class='select  ng-binding']")

    def get_quantity_list(self): # get the list composed of product quantities in the cart page
        rows = self.get_elements(By.TAG_NAME, "tr")
        list_quantities = []
        for row in range(1 ,len(rows)-1): # starting from the 1th row, to the number of rows minus header row
            if row == len(rows):
                break
            list_quantities += [self.get_element(By.XPATH, f"//table/tbody/tr[{row}]/td[5]").text]
        return list_quantities
