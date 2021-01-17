from selenium.webdriver.common.by import By
from config import MAIN_PAGE_URL
from Web_Pages.PageBase import PageBase
from Config.Driver import driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Main_Page(PageBase):
    categories = {"headphones": "#headphonesImg", "mice": "#miceImg", "laptops": "#laptopsImg",
                  "speakers": "#speakersImg", "tablets": "#tabletsImg"}

    def __init__(self):
        super().__init__()

    def click_on_category(self, category):
        Cat = self.get_element(By.CSS_SELECTOR, self.categories[category])
        Cat.click()

    @staticmethod
    def get_main_page():
        driver.navigate(MAIN_PAGE_URL)
