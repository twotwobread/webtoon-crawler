from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler

from webtoon_crawler.utils import join_with_root, make_directory

MAX_LOG_FILE_SIZE = 1024 * 1024 * 100  # 100 MB
DEBUG_LOG_PATH = join_with_root("logs/debug")
ERROR_LOG_PATH = join_with_root("logs/error")
make_directory(DEBUG_LOG_PATH)
make_directory(ERROR_LOG_PATH)


class DateBasedRotatingFileHandler(RotatingFileHandler):
    def emit(self, record):
        current_date = datetime.now().strftime("%Y%m%d")
        new_base_filename = f"{current_date}.log"

        if self.baseFilename != new_base_filename:
            self.baseFilename = new_base_filename
            self._open()

        RotatingFileHandler.emit(self, record)


def get_console_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


def get_file_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    error_handler = DateBasedRotatingFileHandler(
        f'logs/error/{datetime.now().strftime("%Y%m%d")}.log',
        maxBytes=MAX_LOG_FILE_SIZE,
        backupCount=10,
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    debug_handler = DateBasedRotatingFileHandler(
        f'logs/debug/{datetime.now().strftime("%Y%m%d")}.log',
        maxBytes=MAX_LOG_FILE_SIZE,
        backupCount=10,
    )
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)

    logger.addHandler(error_handler)
    logger.addHandler(debug_handler)

    return logger
