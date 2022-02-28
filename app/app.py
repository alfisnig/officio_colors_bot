import logging
from constants import LOG_FILE_PATH
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from .gui import ControlPanelWindow
from .bot_controller import BotController
from catalog_api import CatalogController


logging.getLogger(LOG_FILE_PATH)


class App:
    def __init__(self):
        self._app = QApplication()
        self.control_panel: ControlPanelWindow = None
        self._bot_controller: BotController = None
        self._catalog_controller: CatalogController = None

    def init(self):
        self.control_panel = ControlPanelWindow()
        self.control_panel.show()
        self._bot_controller = BotController()
        self._catalog_controller = CatalogController()
        self.init_connections()

    def init_connections(self):
        self.control_panel.start_bot.connect(self._bot_controller.start_bot_process)
        self.control_panel.stop_bot.connect(self._bot_controller.stop_bot_process)
        self.control_panel.add_catalog.connect(self._catalog_controller.load_catalog)

    def exec(self):
        try:
            return self._app.exec()
        except Exception:
            logging.error("Ошибка: ", exc_info=True)
