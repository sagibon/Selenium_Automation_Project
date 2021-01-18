from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase


class PaymentMethod_Page(PageBase):

    def __init__(self):
        super().__init__()
        self.safepay_user = self.get_element(By.CSS_SELECTOR, 'input[name="safepay_username"]')
        self.safepay_password = self.get_element(By.CSS_SELECTOR, 'input[name="safepay_password"]')
        self.paynow_button = self.get_element(By.ID, 'pay_now_btn_SAFEPAY')

    def pay_with_safepay(self):
        self.safepay_user.send_keys("dolev")
        self.safepay_password.send_keys("Aasd123")
        self.paynow_button.click()

    def thank_you(self):
        return self.get_element(By.CSS_SELECTOR, 'span[translate="Thank_you_for_buying_with_Advantage"]').text

