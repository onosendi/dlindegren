"""
    dlindegren
    ~~~~~~~~~~

    uWSGI entry point.
"""
from app.app_factory import create_app
from app.extensions import db

# uWSGI entry point.
app = create_app()


@app.route('/')
def index():
    return 'Hello world'


@app.shell_context_processor
def make_shell_context():
    """ For `flask shell` - enables shell defaults. """
    return {
        'app': app,
        'db': db,
        }
