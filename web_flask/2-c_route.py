#!/usr/bin/python3
# Author: FiraolTulu
""" This 2. C is fun!"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    """This Function Returns some text."""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello():
    """This Function Return other text."""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """This Function replace text with variable."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
