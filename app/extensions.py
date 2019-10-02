'''
    app.extensions
    ~~~~~~~~~~~~~~

    Extensions are instantiated here without an object given to support the
    application factory model. They are ultimately configured in
    :mod:`app.app_factory`.
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_misaka import Misaka  # For Markdown

db = SQLAlchemy()
migrate = Migrate()
misaka = Misaka()
