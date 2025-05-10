import logging
import logging.handlers
import sys

PATH_TO_LOGS = "app.log"
ENCODING = "UTF-8"

STANDART_FORMAT = "%(asctime)s | %(name)-12s - %(levelname)s - %(message)s"
ERROR_FORMAT = (
    "%(asctime)s | %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
DATE_FORMAT = "%d-%m-%Y %H:%M:%S"

METRICS = "metrics"
ROUTERS = "routers"
APP = "app"

LOGGERS = [APP, METRICS, ROUTERS]

logging.basicConfig(
    level=logging.INFO,
    format=STANDART_FORMAT,
    datefmt=DATE_FORMAT,
)


def setup_logging() -> None:
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging.Formatter(STANDART_FORMAT, DATE_FORMAT))
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.addFilter(lambda record: record.levelno <= logging.WARNING)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(logging.Formatter(ERROR_FORMAT, DATE_FORMAT))
    stderr_handler.setLevel(logging.ERROR)

    file_handler = logging.handlers.RotatingFileHandler(
        filename=PATH_TO_LOGS,
        maxBytes=1024 * 1024 * 10,  # 10 MB
        backupCount=2,
        encoding=ENCODING,
    )
    file_handler.setFormatter(logging.Formatter(STANDART_FORMAT, DATE_FORMAT))
    file_handler.setLevel(logging.INFO)
    file_handler.addFilter(lambda record: record.levelno <= logging.WARNING)

    for logger_name in LOGGERS:
        logger = logging.getLogger(logger_name)

        if logger.handlers:
            logger.handlers.clear()

        logger.addHandler(stdout_handler)
        logger.addHandler(stderr_handler)
        logger.propagate = False
