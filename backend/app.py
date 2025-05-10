import logging
import os
import random
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from prometheus_client import start_http_server

from config import PROMETHEUS_PORT
from config.loggers import setup_logging
from logs import error_handler
from metrics import PrometheusMiddleware
from models import GetHealthResponse, GetWordResponse

setup_logging()
logger = logging.getLogger("app")

WORDS_PATH = "./russian_words.txt"


def load_words(path: str) -> list[str]:
    """Загружает слова из файла в память"""
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} not found")

        with open(path, "r", encoding="utf-8") as file:
            words = file.read().split()

        if not words:
            raise ValueError("File is empty")
    except Exception as e:
        raise RuntimeError("Failed to load word list: %s", e) from e
    return words


words: list[str] = load_words(WORDS_PATH)


@asynccontextmanager
async def lifespan(_: FastAPI):
    start_http_server(port=PROMETHEUS_PORT, addr="127.0.0.1")
    logger.info("Prometheus metrics server started on port %d", PROMETHEUS_PORT)
    yield


app = FastAPI(lifespan=lifespan)
app.add_exception_handler(Exception, error_handler)

app.add_middleware(PrometheusMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/",
    tags=["index", "health"],
    summary="Health check",
    response_model=GetHealthResponse,
)
async def index():
    return JSONResponse(content={"status": "ok"})


@app.get(
    "/get_random_word",
    tags=["words"],
    summary="Get a random word",
    response_model=GetWordResponse,
)
async def get_random_word():
    word = random.choice(words).upper()
    return JSONResponse(content={"word": word})
