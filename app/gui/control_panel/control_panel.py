from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import Signal
from .control_panel_ui import Ui_control_panel


class ControlPanelWindow(QMainWindow):
    start_bot = Signal()
    stop_bot = Signal()
    add_catalog = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_control_panel()
        self._ui.setupUi(self)
        self._init_connectinons()

    def _init_connectinons(self):
        self._ui.start_bot_button.clicked.connect(self._on_start_bot)
        self._ui.stop_bot_button.clicked.connect(self._on_stop_bot)
        self._ui.add_catalog_button.clicked.connect(self._on_add_catalog)

    def _on_start_bot(self):
        self.start_bot.emit()
        self._ui.stop_bot_button.setEnabled(True)
        self._ui.start_bot_button.setEnabled(False)

    def _on_stop_bot(self):
        self.stop_bot.emit()
        self._ui.stop_bot_button.setEnabled(False)
        self._ui.start_bot_button.setEnabled(True)

    def _on_add_catalog(self):
        zip_path, _ = QFileDialog.getOpenFileName(self, caption="Load catalog from .zip", filter=".zip files (*.zip)")
        if not zip_path:
            return None
        self.add_catalog.emit(zip_path)
