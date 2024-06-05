#!/usr/bin/env python3
""" 3-app Module
"""

from flask import Flask, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'


@app.route('/')
def index():
    """ Renders 3-index template """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port=1245)
