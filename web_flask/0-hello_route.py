#!/usr/bin/python3
"""displays hello HBNB to your localhost
using flask
"""
from flask import Flask


app = Flask("__name__")


@app.route('/', strict_slashes=False)
def welcome():
    """serves a string Hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
