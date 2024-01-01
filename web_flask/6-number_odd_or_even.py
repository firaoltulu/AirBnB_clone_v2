#!/usr/bin/python3
# Author: FiraolTulu
""" This will add fifth view func that displays HTML page if n is int """

from flask import Flask
from flask import render_template


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
    loctext = text.replace("_", " ")
    return "C {}".format(loctext)


@app.route("/python/")
@app.route("/python/<text>")
def python_text(text="is cool"):
    """This Function replace more text with another variable."""
    loctext = text.replace("_", " ")
    return "Python {}".format(loctext)


@app.route("/number/<int:n>")
def number_text(n):
    """This Function replace with int only if given int."""
    locn = str(n)
    return "{} is a number".format(locn)


@app.route("/number_template/<int:n>")
def html_num(n):
    """This Function display html if n is int."""
    locn = str(n)
    return render_template("5-number.html", n=locn)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """This Function display different page depending on var given odd or even."""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
