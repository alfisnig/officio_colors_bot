from .connection import execute_sql, create_database


def create_catalog_table():
    sql = ("CREATE TABLE IF NOT EXISTS materials ("
           "    id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "    name TEXT UNIQUE,"
           "    picture BLOB"
           ");")
    execute_sql(sql)


def init_database():
    create_database()
    create_catalog_table()
