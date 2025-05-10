import time

from fastapi import FastAPI
from prometheus_client import Counter, Gauge, Histogram, start_http_server
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

REQUEST_COUNT = Counter(
    "app_requests_total", "Total request count", ["method", "endpoint", "status"]
)
REQUEST_DURATION = Histogram(
    "app_request_duration_seconds", "Request latency", ["endpoint"]
)
ACTIVE_USERS = Gauge("app_active_users", "Active users")


class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        ACTIVE_USERS.inc()

        response: Response = await call_next(request)

        latency = time.time() - start_time
        endpoint = request.url.path
        REQUEST_DURATION.labels(endpoint=endpoint).observe(latency)
        REQUEST_COUNT.labels(
            method=request.method, endpoint=endpoint, status=response.status_code
        ).inc()
        ACTIVE_USERS.dec()

        return response


def init_metrics(app: FastAPI, addr: str = "0.0.0.0", port: int = 5001):
    start_http_server(port=port, addr=addr)
