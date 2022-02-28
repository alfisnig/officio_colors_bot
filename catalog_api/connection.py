import logging
import sqlite3
from constants import CATALOG_DB_PATH, LOG_FILE_PATH


logging.getLogger(LOG_FILE_PATH)


def create_database():
    connection = sqlite3.connect(CATALOG_DB_PATH)
    connection.close()


def execute_sql(sql_expression: str, parameters: dict = None) -> sqlite3.Cursor:
    with sqlite3.connect(CATALOG_DB_PATH) as connection:
        try:
            if parameters is None:
                result = connection.execute(sql_expression)
            else:
                result = connection.execute(sql_expression, parameters)
        except Exception as e:
            logging.error("Ошибка: ", exc_info=True)
            connection.rollback()
        else:
            connection.commit()
            return result
