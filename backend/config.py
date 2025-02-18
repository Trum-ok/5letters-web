import os
from dotenv import load_dotenv

load_dotenv(override=True)

FLASK_PORT = os.getenv("FLASK_PORT", 8080)
PROMETHEUS_PORT = os.getenv("PROMETHEUS_PORT", 5001)
