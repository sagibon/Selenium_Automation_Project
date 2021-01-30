from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase
from selenium.webdriver.common.actions.pointer_actions import PointerActions
import time
from selenium.common.exceptions import NoSuchElementException


class PaymentMethod_Page(PageBase):

    def __init__(self):
        super().__init__()

    def pay_with_safepay(self):
        self.get_element(By.CSS_SELECTOR, 'input[name="safepay_username"]').send_keys("dolev")  # Username
        self.get_element(By.CSS_SELECTOR, 'input[name="safepay_password"]').send_keys("Aasd123")  # Password
        self.get_element(By.ID, 'pay_now_btn_SAFEPAY').click()  # Click pay now

    def pay_with_mastercredit(self):
        try:
            self.get_element(By.XPATH, '//img[@alt="Master credit"]').click()
            self.get_element(By.CSS_SELECTOR, 'input[id="creditCard"]').send_keys("123456789112")
            self.get_element(By.CSS_SELECTOR, 'input[name="cvv_number"]').send_keys("1234")
            self.get_element(By.CSS_SELECTOR, 'input[name="cardholder_name"]').send_keys("dolev")
            self.get_element(By.XPATH, '//button[@id="pay_now_btn_ManualPayment"]').click()  # Do Not Save The Details
        except NoSuchElementException:
            self.get_element(By.ID, 'pay_now_btn_MasterCredit').click()
        else:
            self.get_element(By.ID, 'pay_now_btn_ManualPayment').click()

    def thank_you(self):
        return self.get_element(By.CSS_SELECTOR, 'span[translate="Thank_you_for_buying_with_Advantage"]').text



