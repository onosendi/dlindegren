"""
    app.app_factory
    ~~~~~~~~~~~~~~~

    Flask application factory.

    This module instantiates and configures a Flask application instance
    via :func:`create_app`.
"""
from flask import Flask
from config import DefaultConfig


def create_app(config=None):
    """ Instantiate and set up Flask application.

    :param config: Configuration object from :mod:`config`
    """
    app = Flask(__name__)
    with app.app_context():
        configure_app(app, config)
    return app


def configure_app(app, config):
    """ Configure Flask application.

    :param app: Flask application instance
    :param config: Configuration object from :mod:`config`
    """
    app.config.from_object(DefaultConfig)
    if config:
        app.config.from_object(config)
