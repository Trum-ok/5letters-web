import logging
import time
from collections.abc import Callable

from fastapi import HTTPException, Request, Response
from fastapi.responses import JSONResponse

logger = logging.getLogger("app")


def log_request_start(request: Request) -> None:
    request.state.start_time = time.time()


def log_request_end(request: Request, response: Response) -> JSONResponse:
    latency = time.time() - request.state.start_time
    logger.info(
        "Request completed",
        extra={
            "route": request.url.path,
            "method": request.method,
            "status": response.status_code,
            "latency": f"{latency:.3f}s",
        },
    )
    return response


async def error_handler(request: Request, exc: Exception) -> JSONResponse:
    """Глобальный обработчик ошибок для FastAPI."""
    logger.error(
        "Unhandled exception",
        extra={"route": request.url.path, "method": request.method},
    )
    status_code = exc.status_code if isinstance(exc, HTTPException) else 500
    return JSONResponse(content={"error": str(exc)}, status_code=status_code)


async def logging_middleware(request: Request, call_next: Callable):
    log_request_start(request)
    try:
        response: Response = await call_next(request)
    except Exception as exc:
        return await error_handler(request, exc)
    return log_request_end(request, response)
