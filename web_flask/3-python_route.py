#!/usr/bin/python3
"""displays hello HBNB and "HBNB"to your localhost
using flask
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    """serves a string Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """serves hbnb to the localhost"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def displayC(text):
    """displays C + the text """
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display2(text=None):
    """display Python + <text>"""
    if text is None:
        text = 'is cool'
        return f"Python {text}"

    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
