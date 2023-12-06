from PySide6.QtCore import QObject


class MainWindowModel(QObject):
    def __init__(self) -> None:
        super().__init__()

        self.title: str = ""
