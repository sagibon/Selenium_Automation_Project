import json

with open(r"C:\Users\sagib\PycharmProjects\Selenium_Automation_Project\config.json") as config:
    config = json.load(config)

DRIVER_PATH = config["driver_path"]
TIMED_OUT = config["timed_out"]
MAIN_PAGE_URL = config["main_page_url"]
TEST_6_ERROR = config["test_6_error_msg"]
PASSWORD = config["password"]
USERNAME = config["username"]

file = open(r"C:\Users\sagib\PycharmProjects\Selenium_Automation_Project\RESULTS.txt", "w")
