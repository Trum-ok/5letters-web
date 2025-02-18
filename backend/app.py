import random
import argparse

from flask_cors import CORS
from flask import Flask, jsonify, Response
# from elasticsearch import Elasticsearch

from metrics import init_metrics
from config import FLASK_PORT, PROMETHEUS_PORT
from logs import logger, log_action, log_request_start, log_request_end, error_handler

app = Flask(__name__)
cors = CORS(app)
# es = Elasticsearch(["elasticsearch:9200"], timeout=30)

# TODO: стоит ли всегда хранить его в считанном виде?
with open("russian_words.txt", "r") as txt_file:  
    words = txt_file.read().split()


@app.route("/", methods=["GET"])
@log_action("main page")
def index() -> Response:
    return jsonify({"status": "ok"}), 200


@app.route("/get_random_word", methods=["GET"])
@log_action("get random word")
def get_random_word() -> Response:
    random_word = random.choice(words).upper()
    print(
        f'''
        word: {random_word}
        ''')
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=FLASK_PORT, type=int)
    parser.add_argument("--promport", default=PROMETHEUS_PORT, type=int)
    parser.add_argument("--debug", default=False, type=bool)
    args = parser.parse_args()
    
    init_metrics(app, port=args.promport)

    app.debug = args.debug
    app.run(host="0.0.0.0", port=args.port)


if __name__ == "__main__":
    main()
