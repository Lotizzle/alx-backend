#!/usr/bin/env python3
"""
A flask app that uses babel to to configure
available languages in our app.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Configuration for available languages in our app """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """ Renders the index template """

    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
