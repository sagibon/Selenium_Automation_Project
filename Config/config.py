import json

with open(r"C:\Users\Dolev\Desktop\SeleniumDolevSagi_new\config.json") as config:
    config = json.load(config)

DRIVER_PATH = config["driver_path"]
TIMED_OUT = config["timed_out"]
MAIN_PAGE_URL = config["main_page_url"]
TEST_6_ERROR = config["test_6_error_msg"]
USERNAME = config["username"]
PASSWORD = config["password"]

file = open(r"C:\Users\Dolev\Desktop\SeleniumDolevSagi_new\RESULTS.txt", "w")
