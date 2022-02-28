from typing import Union
from .connection import execute_sql


def add_material_to_db(picture_name: str, picture_object: bytes):
    params = {
        "name": picture_name,
        "picture": picture_object
    }
    sql = ("INSERT INTO materials (name, picture)"
           "    VALUES (:name, :picture)")
    execute_sql(sql, params)


def delete_all_materials():
    sql = "DELETE FROM materials"
    execute_sql(sql)


def get_material_by_name(picture_name: str) -> Union[bytes, None]:
    params = {
        "name": picture_name
    }
    sql = ("SELECT name, picture"
           "    FROM materials"
           "    WHERE name = :name"
           "    COLLATE NOCASE"
           )
    picture = execute_sql(sql, params)
    if picture == []:
        return None
    else:
        return picture[0]
