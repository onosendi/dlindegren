'''
    app.blog.views
    ~~~~~~~~~~~~~~

    End points for blog.
'''
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from app.blog.models import BlogArticle

blog = Blueprint('blog', __name__)


@blog.route('/')
def index():
    articles = BlogArticle.query.order_by(BlogArticle.created.desc()).all()
    return render_template('blog/index.html', articles=articles)


@blog.route('/article/<string:file_name>')
def article(file_name):
    article = BlogArticle.query.filter_by(file_name=file_name).first_or_404()
    try:
        return render_template('/blog/articles/{}.html'.format(file_name),
                           article=article)
    except TemplateNotFound:
        abort(404)
