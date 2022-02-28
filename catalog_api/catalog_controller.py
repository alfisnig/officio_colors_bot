import os
from typing import Union
from .catalog_parser import load_catalog_from_zip
from .db_tools import get_material_by_name


colors_catalog = []


class CatalogController:
    def __init__(self):
        pass

    def load_catalog(self, catalog_path: str):
        load_catalog_from_zip(catalog_path)

    def get_material_by_name(self, material_name) -> Union[bytes, None]:
        return get_material_by_name(material_name)
