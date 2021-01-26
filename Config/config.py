import json

with open("../config.json") as config:
    config = json.load(config)

DRIVER_PATH = config["driver_path"]
TIMED_OUT = config["timed_out"]
MAIN_PAGE_URL = config["main_page_url"]
TEST_6_ERROR = config["test_6_error_msg"]





