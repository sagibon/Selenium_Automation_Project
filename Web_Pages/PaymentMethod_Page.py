from selenium.webdriver.common.by import By
from Web_Pages.PageBase import PageBase



class PaymentMethod_Page(PageBase):

    def __init__(self):
        super().__init__()
        """" SafePay """
        self.safepay_user = self.get_element(By.CSS_SELECTOR, 'input[name="safepay_username"]')
        self.safepay_password = self.get_element(By.CSS_SELECTOR, 'input[name="safepay_password"]')
        self.paynow_button_safepay = self.get_element(By.ID, 'pay_now_btn_SAFEPAY')

    def pay_with_safepay(self):
        self.safepay_user.send_keys("dolev")
        self.safepay_password.send_keys("Aasd123")
        self.paynow_button_safepay.click()

    def pay_with_mastercredit(self):
        self.get_element(By.XPATH, '//div/div[3]/div/div[1]/div[2]/input').click()
        self.get_element(By.CSS_SELECTOR, 'input[id="creditCard"]').send_keys("123456789112")
        self.get_element(By.CSS_SELECTOR, 'input[name="cvv_number"]').send_keys("123")
        self.get_element(By.CSS_SELECTOR, 'input[name="cardholder_name"]').send_keys("dolev")
        self.get_element(By.ID, 'pay_now_btn_ManualPayment')

    def thank_you(self):
        return self.get_element(By.CSS_SELECTOR, 'span[translate="Thank_you_for_buying_with_Advantage"]').text



