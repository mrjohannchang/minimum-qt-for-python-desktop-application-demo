import importlib.resources
import os
import sys

from PySide6.QtCore import Qt, QCoreApplication, QIODevice, QFile
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

from . import ui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


def main() -> int:
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app: QApplication = QApplication(sys.argv)
    with importlib.resources.path(ui.__package__, 'main_window.ui') as main_window_ui:
        ui_file: QFile = QFile(str(main_window_ui))
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {main_window_ui}: {ui_file.errorString()}", file=sys.stderr)
            return 1 if os.name == 'nt' else os.EX_SOFTWARE
        loader: QUiLoader = QUiLoader()
        window: QMainWindow = loader.load(ui_file)
        ui_file.close()
        if not window:
            print(loader.errorString(), file=sys.stderr)
            return 1 if os.name == 'nt' else os.EX_SOFTWARE
        window.show()
        sys.exit(app.exec_())
