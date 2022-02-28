import json
import logging
from constants import JSON_FILE_PATH, LOG_FILE_PATH


logging.getLogger(LOG_FILE_PATH)

with open(JSON_FILE_PATH, "r", encoding="UTF-8") as json_file:
    json_config: dict = json.load(json_file)


API_TOKEN = json_config.get("API_TOKEN", None)
if API_TOKEN is None:
    logging.error(f'API_TOKEN HAS NO VALUE IN JSON FILE f"{JSON_FILE_PATH}"')

REPLY_KEYBOARDS = json_config.get("REPLY_KEYBOARDS", [])
