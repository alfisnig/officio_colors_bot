import os
from typing import List, Tuple
import zipfile
from .db_tools import add_material_to_db, delete_all_materials


def get_pictures_from_zip(path: str) -> List[Tuple[str, bytes]]:
    pictures: List[Tuple[str, bytes]] = []
    with zipfile.ZipFile(path, "r") as zip_file:
        for name in zip_file.namelist():
            if name.endswith((".jpg", ".jpeg", ".png")):
                picture = zip_file.open(name)
                picture_name = os.path.basename(name)
                picture_name = picture_name[:picture_name.rfind(".")]
                pictures.append((picture_name, picture.read()))
    return pictures


def load_materials_to_db(pictures: List[Tuple[str, bytes]]):
    for name, picture_object in pictures:
        add_material_to_db(name, picture_object)


def load_catalog_from_zip(path: str):
    pictures = get_pictures_from_zip(path)
    delete_all_materials()
    load_materials_to_db(pictures)
