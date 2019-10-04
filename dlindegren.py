'''
    dlindegren
    ~~~~~~~~~~

    uWSGI entry point.
'''
import os
import config
from app.app_factory import create_app
from app.extensions import db
from app.admin.models import AdminUser, register_user
from app.blog.models import BlogArticle, BlogCategory

# uWSGI entry point.
if os.environ.get('FLASK_ENV') == 'production':
    app = create_app(config.ProductionConfig)
else:
    app = create_app()


@app.shell_context_processor
def make_shell_context():
    ''' For `flask shell` - enables shell defaults. '''
    return {'app': app,
            'db': db,
            'AdminUser': AdminUser,
            'register_user': register_user,
            'BlogArticle': BlogArticle,
            'BlogCategory': BlogCategory}
