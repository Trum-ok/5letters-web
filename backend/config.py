import os

from dotenv import load_dotenv

load_dotenv(override=True)

PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT", "5001"))
