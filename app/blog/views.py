'''
    app.blog.views
    ~~~~~~~~~~~~~~

    End points for blog.
'''
from flask import Blueprint, render_template

blog = Blueprint('blog', __name__)


@blog.route('/')
def index():
    return render_template('blog/index.html')


@blog.route('/<article>')
def article(article):
    return '{}'.format(article)
