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
        configure_extensions(app)
        configure_blueprints(app)
    return app


def configure_app(app, config):
    """ Configure Flask application.

    :param app: Flask application instance
    :param config: Configuration object from :mod:`config`
    """
    app.config.from_object(DefaultConfig)
    if config:
        app.config.from_object(config)


def configure_extensions(app):
    """ Configure extensions.

    :param app: Flask application instance
    """
    from app.extensions import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)


def configure_blueprints(app):
    from app.views import static
    from app.blog.views import blog
    from app.misc.views import misc
    app.register_blueprint(static)
    app.register_blueprint(blog, subdomain='blog')
    app.register_blueprint(misc, subdomain='misc')
