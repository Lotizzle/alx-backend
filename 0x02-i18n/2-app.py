#!/usr/bin/env python3
"""
This module contains a flask app translates text into
a users preferred language
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
from locale import getdefaultlocale

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Configuration for available languages in our app """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Determines the best match using locale and config """
    user_preferred_languages = [x.replace('-', '_')
                                for x in getdefaultlocale()]
    if user_preferred_language[0] in app.config['LANGUAGES']:
        return user_preferred_languages[0]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Renders the index template """

    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
