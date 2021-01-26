from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase
from Web_Pages.CreateAccount_Page import CreateAccount


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

    def login_with_exist_user(self, ):
        self.username.send_keys(CreateAccount.new_username)
        self.password.send_keys(CreateAccount.new_password)
        self.login_button.click()

    def click_next(self):
        self.get_element(By.XPATH, '//*[@id="next_btn"]').click()