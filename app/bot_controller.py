import multiprocessing as mp
from PySide6.QtCore import QObject, Signal
from bot import start_bot, stop_bot


class BotController(QObject):
    def __init__(self):
        self.process: mp.Process = None

    def _start_process(self):
        self.process = mp.Process(target=start_bot)
        self.process.start()

    def _stop_process(self):
        stop_bot()
        self.process.terminate()
        self.process.join()
        self.process.close()
        self.process = None

    def start_bot_process(self):
        self._start_process()

    def stop_bot_process(self):
        self._stop_process()
