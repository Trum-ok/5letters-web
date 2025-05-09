import random
from pathlib import Path

from flask import Flask, Response, jsonify
from flask_cors import CORS

from config import PROMETHEUS_PORT
from logs import error_handler, log_action, log_request_end, log_request_start, logger

# from elasticsearch import Elasticsearch
from metrics import init_metrics

app = Flask(__name__)
app.logger = logger
cors = CORS(app)
# es = Elasticsearch(["elasticsearch:9200"], timeout=30)

_words: list[str] = []


def load_words() -> None:
    """Загружает слова из файла в память"""
    global _words
    try:
        file_path = Path("russian_words.txt")
        _words = file_path.read_text(encoding="utf-8").split()
        if not _words:
            raise ValueError("File is empty")
    except Exception as e:
        app.logger.error(f"Error loading words: {str(e)}")
        exit(1)


@app.route("/", methods=["GET"])
@log_action("main page")
def index() -> Response:
    return jsonify({"status": "ok"}), 200


@app.route("/get_random_word", methods=["GET"])
@log_action("get random word")
def get_random_word() -> Response:
    random_word = random.choice(_words).upper()
    app.logger.info(f"get_random_word: {random_word}")
    return jsonify({"word": random_word}), 200


@app.before_request
def br() -> None:
    log_request_start()


@app.after_request
def ar(response):
    return log_request_end(response)


@app.errorhandler(Exception)
def handle_exception(e):
    return error_handler(e)


def prod_app():
    # init_metrics(app, PROMETHEUS_PORT)
    load_words()
    app.debug = False
    return app


app = prod_app()

## uncomment to run without docker & gunicorn
# import argparse
#
# def local_main() -> None:
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--port", default=FLASK_PORT, type=int)
#     parser.add_argument("--promport", default=PROMETHEUS_PORT, type=int)
#     parser.add_argument("--debug", default=False, type=bool)
#     args = parser.parse_args()

#     init_metrics(app, port=args.promport)
#     load_words()

#     app.debug = args.debug
#     app.run(host="0.0.0.0", port=args.port)
#
#
# if __name__ == "__main__":
#     local_main()
