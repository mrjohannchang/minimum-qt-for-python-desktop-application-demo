import logging
import sys

from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QApplication

from . import ui
from . import ui_model


def main() -> int:
    logging.basicConfig()
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app: QApplication = QApplication(sys.argv)
    _ = ui.MainWindow().inflate().bind(ui_model.MainWindowModel()).show()
    return app.exec_()
