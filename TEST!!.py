from config import DRIVER_PATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

webdriver.Firefox(executable_path=DRIVER_PATH)