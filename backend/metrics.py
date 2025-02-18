import time

from flask import g, request, Flask
from prometheus_client import start_http_server, Counter, Histogram, Gauge

# Инициализация метрик
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total request count",
    ["method", "endpoint", "status"]
)
REQUEST_DURATION = Histogram(
    "app_request_duration_seconds",
    "Request latency",
    ["endpoint"]
)
ACTIVE_USERS = Gauge(
    "app_active_users",
    "Active users"
)

def init_metrics(app: Flask, port=5001):
    # Регистрация хуков
    @app.before_request
    def track_request_start():
        g.start_time = time.time()
        ACTIVE_USERS.inc()

    @app.after_request
    def track_request_end(response):
        latency = time.time() - g.start_time
        REQUEST_DURATION.labels(request.path).observe(latency)
        REQUEST_COUNT.labels(
            request.method,
            request.path,
            response.status_code
        ).inc()
        ACTIVE_USERS.dec()
        return response
    
    # Запуск сервера метрик
    start_http_server(port)
