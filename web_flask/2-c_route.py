#!/usr/bin/python3
"""
Scripts starts a simple flask application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """function def for routing"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    route for hbnb
    displays "HBNB'
    """
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    n_text = text.replace('_', ' ')
    return f'C {n_text}'


if __name__ == "__main__":
    app.run(debug=True)
