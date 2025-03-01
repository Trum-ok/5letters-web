import os
import sys
# import multiprocessing

GUNICORN_PORT = os.getenv('GUNICORN_PORT')

if not GUNICORN_PORT:
    sys.stderr.write("[ERROR] GUNICORN_PORT environment variable is not set\n")
    sys.exit(1)

try:
    GUNICORN_PORT = int(GUNICORN_PORT)
except ValueError:
    sys.stderr.write(f"[ERROR] Invalid port format: {GUNICORN_PORT}\n")
    sys.exit(1)

bind = f"0.0.0.0:{GUNICORN_PORT}"
workers = 4
worker_class = "gevent"
timeout = 15
keepalive = 5
max_requests = 200
max_requests_jitter = 50
loglevel = "info"
accesslog = "-"  # stdout
errorlog = "-"   # stdout

# accesslog = "/var/log/flask/access.log"  # stdout
# errorlog = "/var/log/flask/error.log"   # stdout