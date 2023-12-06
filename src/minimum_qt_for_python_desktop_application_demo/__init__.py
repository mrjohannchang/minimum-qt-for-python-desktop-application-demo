import importlib.metadata

from .log import get_logger, init_logger

VERSION: str = importlib.metadata.version("minimum-qt-for-python-desktop-application-demo")
