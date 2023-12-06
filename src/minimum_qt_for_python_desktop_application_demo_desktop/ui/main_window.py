import minimum_qt_for_python_desktop_application_demo as sdk
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow, QPushButton


class QMainWindowExt(QMainWindow):
    def closeEvent(self, event: QCloseEvent) -> None:
        sdk.get_logger().info(f"Close event: {event}")
        super().closeEvent(event)

    def set_up(self) -> None:
        sdk.get_logger().info("Setting up")
        self.setWindowTitle(f"Minimum Qt for Python Desktop Application v{sdk.VERSION}")

        # The following line is optional. This is only for the IDE to recognize the push_button attribute.
        self.push_button: QPushButton = getattr(self, 'push_button')

        self.push_button.clicked.connect(self.on_push_button_clicked_listener)

    def on_push_button_clicked_listener(self, checked: bool) -> None:
        sdk.get_logger().info(f"Push button clicked, checked: {checked}")
