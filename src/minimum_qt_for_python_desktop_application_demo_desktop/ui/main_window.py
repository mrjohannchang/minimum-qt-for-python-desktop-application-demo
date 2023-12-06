import minimum_qt_for_python_desktop_application_demo as sdk
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow


class QMainWindowExt(QMainWindow):
    def closeEvent(self, event: QCloseEvent) -> None:
        sdk.get_logger().info(f"Close event: {event}")
        super().closeEvent(event)
