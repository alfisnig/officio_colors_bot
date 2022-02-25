from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from .gui import ControlPanelWindow
from bot import start_bot, stop_bot


class App:
    def __init__(self):
        self._app = QApplication()
        self.control_panel: ControlPanelWindow = None

    def init(self):
        self.control_panel = ControlPanelWindow()
        self.control_panel.show()
        self.init_connections()

    def init_connections(self):
        self.control_panel.start_bot.connect(start_bot)
        self.control_panel.stop_bot.connect(stop_bot)

    def exec(self):
        try:
            return self._app.exec()
        except Exception:
            return self._app.exec_()
