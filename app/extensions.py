'''
    app.extensions
    ~~~~~~~~~~~~~~

    Extensions are instantiated here without an object given to support the
    application factory model. They are ultimately configured in
    :mod:`app.app_factory`.
'''
from flask_misaka import Misaka  # For Markdown

misaka = Misaka()
