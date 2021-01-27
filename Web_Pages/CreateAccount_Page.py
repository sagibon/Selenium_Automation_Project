from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase
from random_words import RandomEmails
from random_words import RandomNicknames
from Config.config import PASSWORD


class CreateAccount(PageBase):

    new_username = ""
    new_password = ""

    def __init__(self):
        super().__init__()
        self.username = self.get_element(By.CSS_SELECTOR, 'input[name="usernameRegisterPage"]')
        self.email = self.get_element(By.CSS_SELECTOR, 'input[name="emailRegisterPage"]')
        self.password = self.get_element(By.CSS_SELECTOR, 'input[name="passwordRegisterPage"]')
        self.confirm_password = self.get_element(By.CSS_SELECTOR, 'input[name="confirm_passwordRegisterPage"]')
        self.agree_button = self.get_element(By.CSS_SELECTOR, 'input[name="i_agree"]')
        self.register_button = self.get_element(By.CSS_SELECTOR, '#register_btnundefined')
        self.generate_email = RandomEmails()
        self.generate_username = RandomNicknames()

    def enter_valid_details(self):
        password = PASSWORD
        username = self.generate_username.random_nicks()
        email = self.generate_email.randomMail()
        self.username.send_keys(username)
        self.email.send_keys(email)
        self.password.send_keys(password)
        self.confirm_password.send_keys(password)
        self.agree_button.click()
        self.register_button.click()
        return [username, password]

