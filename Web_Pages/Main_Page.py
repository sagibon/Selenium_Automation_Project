from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Config.config import MAIN_PAGE_URL, PASSWORD
from Web_Pages.PageBase import PageBase
from random_words import RandomEmails
from random_words import RandomNicknames
from Config.Driver import driver


class Main_Page(PageBase):
    categories = {"headphones": "#headphonesImg", "mice": "#miceImg", "laptops": "#laptopsImg",
                  "speakers": "#speakersImg", "tablets": "#tabletsImg"}

    def __init__(self):
        super().__init__()
        self.generate_email = RandomEmails()
        self.generate_username = RandomNicknames()

    def click_on_category(self, category):
        self.element_not_exist(By.XPATH, '//div[@class="loader"]')
        Cat = self.get_element(By.CSS_SELECTOR, self.categories[category])
        Cat.click()

    def stop_instance(self):
        self.driver.stop_instance()

    def get_main_page(self):
        driver.navigate(MAIN_PAGE_URL)

    def check_user_orders(self):
        self.get_element(By.ID, 'menuUserSVGPath').click()
        self.element_not_exist(By.CSS_SELECTOR, 'div[class="emptyCart"]')
        self.get_element(By.XPATH, '//div/label[@translate="My_Orders"][@role="link"]').click()
        return self.get_element(By.CSS_SELECTOR, 'span[class="ng-binding"]').text

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

    def click_to_login_from_main_page(self, username, password):
        self.get_element(By.ID, "menuUser").click()
        self.get_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)
        self.get_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
        self.get_element(By.ID, "sign_in_btnundefined").click()  # click on sign in

    def logout_user(self):
        self.get_element(By.ID, "hrefUserIcon").click()
        self.get_element(By.CSS_SELECTOR, "div[id='loginMiniTitle']>label[translate='Sign_out']").click()

    def check_login_name(self):
        try:
            return self.get_element(By.CSS_SELECTOR,
                                    "a[id='menuUserLink']>span[data-ng-show='userCookie.response']").text
        except NoSuchElementException:
            return "out"
