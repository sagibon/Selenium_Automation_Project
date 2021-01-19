from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase


class PaymentMethod_Page(PageBase):

    def __init__(self):
        super().__init__()
        """" SafePay """
        self.safepay_user = self.get_element(By.CSS_SELECTOR, 'input[name="safepay_username"]')
        self.safepay_password = self.get_element(By.CSS_SELECTOR, 'input[name="safepay_password"]')
        self.paynow_button_safepay = self.get_element(By.ID, 'pay_now_btn_SAFEPAY')
        self.paynow_button_mastercredit = self.get_element(By.ID, 'pay_now_btn_ManualPayment')
        """" MasterCredit """
        self.mastercredit_button = self.get_element(By.CSS_SELECTOR, 'input[name="masterCredit"]')
        self.card_number = self.get_element(By.CSS_SELECTOR, 'input[id="creditCard"]')
        self.cvv_number = self.get_element(By.CSS_SELECTOR, 'input[name="cvv_number"]')
        self.card_holdername = self.get_element(By.CSS_SELECTOR, 'input[name="cardholder_name"]')

    def pay_with_safepay(self):
        self.safepay_user.send_keys("dolev")
        self.safepay_password.send_keys("Aasd123")
        self.paynow_button_safepay.click()

    def pay_with_mastercredit(self):
        self.mastercredit_button.click()
        self.card_number.send_keys("123456789112")
        self.cvv_number.send_keys("123")
        self.card_holdername.send_keys("dolev")
        self.paynow_button_mastercredit.click()

    def thank_you(self):
        return self.get_element(By.CSS_SELECTOR, 'span[translate="Thank_you_for_buying_with_Advantage"]').text



