#!/usr/bin/python3
"""displays hello HBNB and "HBNB"to your localhost
using flask
"""
from flask import Flask, render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def id_render(n):
    """display number if its an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_render(n):
    """show template of n"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """check if value is odd or even"""
    outcome = "odd"
    if n % 2 == 0:
        outcome = "even"
        return render_template("6-number_odd_or_even.html", n=n,
                               outcome=outcome)
    return render_template("6-number_odd_or_even.html", n=n, outcome=outcome)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
