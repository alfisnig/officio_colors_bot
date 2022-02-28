import os
from .catalog_parser import load_catalog_from_zip


colors_catalog = []


class CatalogController:
    def __init__(self):
        pass

    def get_color_by_string(self, text: str):
        string_has_number = text.split(" ")[-1].isdigit()

    def load_catalog(self, catalog_path: str):
        load_catalog_from_zip(catalog_path)
