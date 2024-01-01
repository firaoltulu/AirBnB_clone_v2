#!/usr/bin/python3
# Author: FiraolTulu
""" This 3. Python is cool!"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbn():
    """This function will return Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This function will return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_var(text):
    """This function will display text variable passed in"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def text_var_python(text="is cool"):
    """This will function to display text variable, with default "is cool" """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)