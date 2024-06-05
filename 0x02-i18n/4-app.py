#!/usr/bin/env python3
"""
4-app module
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

# Configure Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

@babel.localeselector
def get_locale():
    """
    Select the best match for supported locales.
    If a locale parameter is provided in the URL, use it if it's supported.
    """
    locale = request.args.get('locale')
    if locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@app.route('/')
def index():
    """
    Route to render the home page.

    This function renders the home page template, which includes
    translated strings using the gettext function.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template('4-index.html')

if __name__ == "__main__":
    app.run(port=5000)
