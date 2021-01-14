import json

with open("../config.json") as config:
    config = json.load(config)

DRIVER_PATH = config["driver_path"]
