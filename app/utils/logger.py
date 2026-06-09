import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.INFO: "\033[92m",
        logging.WARNING: "\033[93m",
        logging.ERROR: "\033[91m",
        logging.DEBUG: "\033[94m",
    }
    RESET = "\033[0m"

    def format(self, record):
        msg = super().format(record)
        color = self.COLORS.get(record.levelno, "")
        return f"{color}{msg}{self.RESET}" if color else msg


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("app_logger")
        self.logger.setLevel(logging.INFO)

        if self.logger.handlers:
            return

        fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        datefmt = "%Y-%m-%d %H:%M:%S"

        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

        console = logging.StreamHandler()
        console.setFormatter(ColoredFormatter(fmt=fmt, datefmt=datefmt))

        file_handler = RotatingFileHandler(
            os.path.join(LOG_DIR, "app.log"),
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
        )
        file_handler.setFormatter(formatter)

        error_handler = RotatingFileHandler(
            os.path.join(LOG_DIR, "error.log"),
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
        )
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)

        self.logger.addHandler(console)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(error_handler)

    def get_logger(self):
        return self.logger


logger = Logger().get_logger()