import os
import multiprocessing

port = os.getenv('GUNICORN_PORT', 5000)

bind = f"0.0.0.0:{port}"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
timeout = 30
keepalive = 5
max_requests = 200
max_requests_jitter = 50
loglevel = "info"
accesslog = "-"  # stdout
errorlog = "-"   # stdout
