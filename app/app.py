from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from .gui import ControlPanelWindow
from .bot_controller import BotController


class App:
    def __init__(self):
        self._app = QApplication()
        self.control_panel: ControlPanelWindow = None
        self._bot_controller: BotController = None

    def init(self):
        self.control_panel = ControlPanelWindow()
        self.control_panel.show()
        self._bot_controller = BotController()
        self.init_connections()

    def init_connections(self):
        self.control_panel.start_bot.connect(self._bot_controller.start_bot_process)
        self.control_panel.stop_bot.connect(self._bot_controller.stop_bot_process)

    def exec(self):
        try:
            return self._app.exec()
        except Exception:
            return self._app.exec_()
