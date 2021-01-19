from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase


class Cart_Page(PageBase):

    def __init__(self):
        super().__init__()

    def get_price(self):
        return self.get_element(By.ID, "checkOutButton")

    def go_to_cart(self):
        self.get_element(By.ID, "menuCart").click()

    def get_page_path(self):  # checks the path in the left side of the page nav bar
        return self.check_page_path(By.CSS_SELECTOR, "nav[class='pages fixedImportant'] a[class='select  ng-binding']")

    def get_quantity_list(self): # get the list composed of product quantities in the cart page
        rows = self.get_elements(By.CSS_SELECTOR, "tr[class='ng-scope']")
        list_quantities = []
        for row in range(1, len(rows)-1):  # starting from the 1th row, to the number of rows minus header row
            if row == len(rows):
                break
            list_quantities += [self.get_element(By.XPATH, f"//table/tbody/tr[{row}]/td[5]").text]
        return list_quantities

    def edit_quantity(self, row): # edits the product quantity in a specific row in cart page summary table
        self.get_element(By.XPATH, f"//table/tbody/tr[{row}]/td[6]/span/a[@class='edit ng-scope']").click()

    def check_user_orders(self):
        self.get_element(By.ID, 'menuUserSVGPath').click()
        self.element_not_exist(By.CSS_SELECTOR, 'div[class="emptyCart"]')
        self.get_element(By.XPATH, '//div/label[@translate="My_Orders"][@role="link"]').click()
        return self.get_element(By.CSS_SELECTOR, 'span[class="ng-binding"]').text

