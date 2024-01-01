#!/usr/bin/python3
# Author: Firaoltulu
""" This 1. HBNB"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """This Function Returns some text."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    """This Function Return other text."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
