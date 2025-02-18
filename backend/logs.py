import time
import logging

from functools import wraps
from werkzeug.exceptions import HTTPException
from flask import request, g, jsonify, Response
from pythonjsonlogger.json import JsonFormatter

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = JsonFormatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s %(route)s %(method)s %(status)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


def log_action(action_name):
    def decorator(func):
        @wraps(func)  # Сохраняем метаданные оригинальной функции
        def wrapper(*args, **kwargs):
            logger.info(f"Action started: {action_name}", extra={
                "route": request.path,
                "method": request.method,
                "status": "started"
            })
            result = func(*args, **kwargs)
            logger.info(f"Action completed: {action_name}", extra={
                "route": request.path,
                "method": request.method,
                "status": "completed"
            })
            return result
        return wrapper
    return decorator


def log_request_start() -> None:
    g.start_time = time.time()
    logger.info("Request started", extra={
        "route": request.path,
        "method": request.method,
        "status": "started"
    })


def log_request_end(response):
    latency = time.time() - g.start_time
    logger.info("Request completed", extra={
        "route": request.path,
        "method": request.method,
        "status_code": response.status_code,
        "latency": f"{latency:.3f}s"
    })
    return response


def error_handler(error) -> tuple[Response, int]:
    logger.error("Unhandled exception", exc_info=True)
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
    return jsonify(error=str(error)), code
