import os
from constants import ROOT_DIR, CATALOG_DIR_NAME


colors_catalog = []


class CatalogController:
    def __init__(self):
        pass

    def get_color_by_string(self, text: str):
        string_has_number = text.split(" ")[-1].isdigit()


