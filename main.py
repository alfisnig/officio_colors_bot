from app import App
import logging
from constants import LOG_FILE_PATH
from catalog_api import init_database


logging.basicConfig(filename=LOG_FILE_PATH, level=logging.DEBUG, format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
init_database()


if __name__ == '__main__':
    app = App()
    app.init()
    app.exec()
