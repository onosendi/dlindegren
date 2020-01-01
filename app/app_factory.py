'''
    app.app_factory
    ~~~~~~~~~~~~~~~

    Flask application factory.

    This module instantiates and configures a Flask application instance.
'''
from flask import Flask
from config import DefaultConfig


def create_app(config=None):
    app = Flask(__name__)
    with app.app_context():
        configure_app(app, config)
        configure_extensions(app)
        configure_blueprints(app)
        configure_jinja(app)
    return app


def configure_app(app, config):
    app.config.from_object(DefaultConfig)
    if config:
        app.config.from_object(config)


def configure_extensions(app):
    ''' Extensions go here. '''

def configure_blueprints(app):
    from app.views import dlindegren
    app.register_blueprint(dlindegren)


def configure_jinja(app):
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.trim_blocks = True
