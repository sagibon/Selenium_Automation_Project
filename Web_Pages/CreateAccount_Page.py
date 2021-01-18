from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase


class CreateAccount(PageBase):

    def __init__(self):
        super().__init__()
        self.username = self.get_element(By.CSS_SELECTOR, 'input[name="usernameRegisterPage"]')
        self.email = self.get_element(By.CSS_SELECTOR, 'input[name="emailRegisterPage"]')
        self.password = self.get_element(By.CSS_SELECTOR, 'input[name="passwordRegisterPage"]')
        self.confirm_password = self.get_element(By.CSS_SELECTOR, 'input[name="confirm_passwordRegisterPage"]')
        self.agree_button = self.get_element(By.CSS_SELECTOR, 'input[name="i_agree"]')
        self.register_button = self.get_element(By.CSS_SELECTOR, '#register_btnundefined')

    def enter_valid_details(self):
        self.username.send_keys("zxfddfffejyr")
        self.email.send_keys("pfersddfrz@poez.com")
        self.password.send_keys("Aasda123")
        self.confirm_password.send_keys("Aasda123")
        self.agree_button.click()
        self.register_button.click()

    def click_next(self):
        self.get_element(By.ID, 'next_btn').click()



# class ShippingMethod_Page(PageBase):
#     def __init__(self):
#         super().__init__()
#         self.next_button = self.get_element(By.ID, 'next_btn')
#
#     def click_next(self):
#         self.next_button.click()

