import logging.handlers
import sys

inited: bool = False


def init_logger() -> None:
    global inited
    if inited:
        return

    logger: logging.Logger = logging.getLogger()
    formatter: logging.Formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    inited = True


def get_logger(name: str = str(__package__)) -> logging.Logger:
    if not inited:
        print('Logger is not initialized yet', file=sys.stderr)
    return logging.getLogger(name)
