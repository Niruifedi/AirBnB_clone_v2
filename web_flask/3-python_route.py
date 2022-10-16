#!/usr/bin/python3
"""
Script starts a simple flask application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """
    Prints a message when / is called in the url
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Prints a message when /hbnb is called in the url
    """
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    """
    Prints a message when /c/<text> is called in the url
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def py_route(text):
    """
    prints a message when /python/<text> is called in the url
    Also prints out the default value of text when /python/ is called
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(debug=True, strict_slashes=False)
