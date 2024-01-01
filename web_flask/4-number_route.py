#!/usr/bin/python3
# Author: FiraolTulu
""" This 4. Is it a number? """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """This function Returns some text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """This function Return other text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """This function will replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """This function will replace more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """This function will replace with int only if given int. """
    n = str(n)
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)