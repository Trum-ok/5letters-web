import logging
import logging.handlers
import os
import time
from functools import wraps
from pathlib import Path

from flask import Response, g, jsonify, request
from pythonjsonlogger.json import JsonFormatter
from werkzeug.exceptions import HTTPException

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = JsonFormatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s %(route)s %(method)s %(status)s",
    json_ensure_ascii=False,
)
handler.setFormatter(formatter)
logger.addHandler(handler)

PATH_TO_LOGS = "/var/log/flask/app.log"

if not os.path.exists(PATH_TO_LOGS):
    log_dir = os.path.dirname(PATH_TO_LOGS)
    Path(log_dir).mkdir(parents=True, exist_ok=True)

file_handler = logging.handlers.RotatingFileHandler(
    PATH_TO_LOGS,
    maxBytes=1024 * 1024 * 10,  # 10 MB
    backupCount=5,
    encoding="utf-8",
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def log_action(action_name):
    def decorator(func):
        @wraps(func)  # Сохраняем метаданные оригинальной функции
        def wrapper(*args, **kwargs):
            logger.info(
                f"Action started: {action_name}",
                extra={
                    "route": request.path,
                    "method": request.method,
                    "status": "started",
                },
            )
            result = func(*args, **kwargs)
            logger.info(
                f"Action completed: {action_name}",
                extra={
                    "route": request.path,
                    "method": request.method,
                    "status": "completed",
                },
            )
            return result

        return wrapper

    return decorator


def log_request_start() -> None:
    g.start_time = time.time()
    logger.info(
        "Request started",
        extra={"route": request.path, "method": request.method, "status": "started"},
    )


def log_request_end(response):
    latency = time.time() - g.start_time
    logger.info(
        "Request completed",
        extra={
            "route": request.path,
            "method": request.method,
            "status_code": response.status_code,
            "latency": f"{latency:.3f}s",
        },
    )
    return response


def error_handler(error) -> tuple[Response, int]:
    logger.error("Unhandled exception", exc_info=True)
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
    return jsonify(error=str(error)), code
