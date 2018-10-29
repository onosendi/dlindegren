"""
    app.extensions
    ~~~~~~~~~~~~~~

    Extensions are instantiated here without an object given to support the
    application factory model. They are ultimately set up in
    :mod:`app.app_factory` via :func:`configure_extensions`.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
