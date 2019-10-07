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
from app.util.testing import (
    load_articles, load_categories, create_fake_articles,
    create_fake_categories)

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
            'BlogCategory': BlogCategory,
            'load_articles': load_articles,
            'load_categories': load_categories,
            'create_fake_articles': create_fake_articles,
            'create_fake_categories': create_fake_categories,
            'a': load_articles(),
            'c': load_categories()}
