import random

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open("russian_words.txt", "r") as txt_file:
    words = txt_file.read().split()


@app.route("/")
def main():
    return "ok"


@app.route("/get_random_word", methods=["GET"])
def get_random_word():
    random_word = random.choice(words).upper()
    print(
        f'''
        word: {random_word}
        ''')
    return jsonify({"word": random_word})


if __name__ == "__main__":
    app.run(port=8080)
