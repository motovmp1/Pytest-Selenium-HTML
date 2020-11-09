import inspect
import logging
import time

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    timer_user_writer = 2

    def timerPages(self):
        time.sleep(self.timer_user_writer)

    def refreshPage(self):
        return self.driver.refresh()

    def test_logginfile(self):
        classmate = inspect.stack()[1][3]
        logger = logging.getLogger(classmate)
        filepath = logging.FileHandler('logFile.log')  # file path
        formatter = logging.Formatter("%(asctime)s;%(message)s;%(levelname)s;%(name)s;style='{'")
        filepath.setFormatter(formatter)  # here pass the formatter
        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(filepath)  # ask the place

        logger.setLevel(logging.DEBUG)

        return logger
