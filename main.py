import logging
import os
from app import App
from constants import LOG_FILE_PATH
from catalog_api import init_database


logging.getLogger(LOG_FILE_PATH)
logging.basicConfig(filename=LOG_FILE_PATH, level=logging.ERROR, format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', filemode="a")
init_database()


if __name__ == '__main__':
    app = App()
    app.init()
    app.exec()
