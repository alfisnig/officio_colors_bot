import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CATALOG_DB_NAME = "catalog.db"
CATALOG_DB_PATH = os.path.join(ROOT_DIR, CATALOG_DB_NAME)
LOG_FILE_NAME = "logs.log"
LOG_FILE_PATH = os.path.join(ROOT_DIR, LOG_FILE_NAME)
