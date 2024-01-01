#!/usr/bin/python3
# Author: FiraolTulu
""" starts a Flask web application """

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ This function will display the states and cities listed in alphabetical order """
    locstates = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=locstates)


@app.teardown_appcontext
def teardown_db(exception):
    """ This will closes the storage on teardown """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')