from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase


class OrderPaymentLogin(PageBase):

    def __init__(self):
        super().__init__()
        self.register_button = self.get_element(By.CSS_SELECTOR, '#registration_btnundefined')
        self.login_button = self.get_element(By.CSS_SELECTOR, '#login_btnundefined')
        self.username = self.get_element(By.CSS_SELECTOR, 'input[name="usernameInOrderPayment"]')
        self.password = self.get_element(By.CSS_SELECTOR, 'input[name="passwordInOrderPayment"]')

    def click_to_register(self):
        # self.element_exists(By.CSS_SELECTOR, '#registration_btnundefined')
        self.register_button.click()