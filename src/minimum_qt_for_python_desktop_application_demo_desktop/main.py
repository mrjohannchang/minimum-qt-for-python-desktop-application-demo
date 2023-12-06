import importlib.resources
import pathlib
import sys

from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow
from . import ui


def main() -> int:
    app: QApplication = QApplication(sys.argv)

    ui_loader: QUiLoader = QUiLoader()

    ui_path: pathlib.Path
    with importlib.resources.path(ui, 'main_window.ui') as ui_path:
        ui_file: QFile = QFile(str(ui_path))
        if not ui_file.open(QIODevice.ReadOnly):
            raise RuntimeError(f"Cannot open {ui_path}: {ui_file.errorString()}")
        main_window: QMainWindow = ui_loader.load(ui_file)
        ui_file.close()
    main_window.show()
    return app.exec_()
