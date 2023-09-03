import os

from webtoon_crawler.utils import logger_config


def test_get_file_logger():
    # given
    file_logger = logger_config.get_file_logger(__name__)
    # when
    file_logger.error("test file logging")
    # then
    assert os.path.exists(logger_config.DEBUG_LOG_PATH)
    assert os.path.exists(logger_config.ERROR_LOG_PATH)


def test_get_console_logger():
    # given
    console_logger = logger_config.get_console_logger(__name__)
    # when
    console_logger.debug("test console logging")
