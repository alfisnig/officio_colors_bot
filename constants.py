import sys
import os
import json


if getattr(sys, 'frozen', False):
    ROOT_DIR = os.path.dirname(sys.executable)
elif __file__:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

CATALOG_DB_NAME = "catalog.db"
CATALOG_DB_PATH = os.path.join(ROOT_DIR, CATALOG_DB_NAME)
LOG_FILE_NAME = "logs.log"
LOG_FILE_PATH = os.path.join(ROOT_DIR, LOG_FILE_NAME)
JSON_FILE_NAME = "config.json"
JSON_FILE_PATH = os.path.join(ROOT_DIR, JSON_FILE_NAME)
JSON_DEFAULT_SCTRUCTURE = {"API_TOKEN": "", "REPLY_KEYBOARDS": ["Aspendos", "Elite", "File Air", "Inter", "Martin",
                                                                "Nil", "Sahra", "Serit Sert File", "Sert Air File",
                                                                "Sert File", "Toskano"]}

# create config .json file if not exist
if not os.path.exists(JSON_FILE_PATH):
    with open(JSON_FILE_PATH, 'w', encoding="UTF-8") as json_file:
        json.dump(JSON_DEFAULT_SCTRUCTURE, json_file, indent=4, sort_keys=True)
