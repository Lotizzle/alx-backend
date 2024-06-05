#!/usr/bin/env python3
"""
Flask application module for internationalization with user emulation.

This module sets up a Flask application with Babel for internationalization
(i18n) support. It includes locale selection based on URL parameters and
browser preferences, and user emulation via URL parameters.

Attributes:
    app (Flask): The Flask application instance.
    babel (Babel): The Babel instance for i18n support.
    users (dict): Mocked user database.

Functions:
    get_locale: Determines the best match for supported locales based on
    URL parameters and browser preferences.

    get_user: Retrieves a user dictionary based on the user ID provided
    in the URL parameters.

    before_request: Sets the current user as a global variable.

    index: Renders the home page with localized content and user information.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

# Configure Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

# Mocked user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """
    Select the best match for supported locales.

    This function checks if a 'locale' parameter is present in the request
    arguments and if its value is among the supported locales. If so, it
    returns that value. Otherwise, it falls back to the best match based on
    the 'Accept-Language' HTTP header.

    Returns:
        str: The locale to use for the current request.
    """
    locale = request.args.get('locale')
    if locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale
    if (
        g.user and
        g.user.get('locale') in app.config['BABEL_SUPPORTED_LOCALES']
    ):
        return g.user['locale']
    return request.accept_languages.best_match(
        app.config['BABEL_SUPPORTED_LOCALES']
    )


def get_user():
    """
    Retrieve a user dictionary based on the user ID provided in the
    URL parameters.

    This function checks if a 'login_as' parameter is present in the request
    arguments and if its value corresponds to a valid user ID in the mocked
    user database. If so, it returns the user dictionary. Otherwise, it
    returns None.

    Returns:
        dict: The user dictionary or None if not found.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Set the current user as a global variable.

    This function is executed before each request. It uses the get_user
    function to find a user based on the 'login_as' parameter and sets
    it as a global variable g.user.
    """
    g.user = get_user()


@app.route('/')
def index():
    """
    Route to render the home page.

    This function renders the home page template, which includes
    translated strings using the gettext function and user information.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port=1245)
