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
