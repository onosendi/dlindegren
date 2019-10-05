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
    from app.extensions import db, migrate, login, misaka
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'admin.login'
    misaka.init_app(app)


def configure_blueprints(app):
    from app.errors.views import errors
    from app.frontend.views import frontend
    from app.admin.views import admin, Blog
    from app.blog.views import blog
    from app.misc.views import misc

    admin.add_url_rule('/blog', view_func=Blog.as_view('blog'))

    app.register_blueprint(errors)
    app.register_blueprint(frontend)
    app.register_blueprint(admin)
    app.register_blueprint(blog, subdomain='blog')
    app.register_blueprint(misc, subdomain='misc')


def configure_jinja(app):
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.trim_blocks = True
