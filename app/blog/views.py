'''
    app.blog.views
    ~~~~~~~~~~~~~~

    End points for blog.
'''
from flask import Blueprint, render_template

blog = Blueprint('blog', __name__)


@blog.route('/')
def home():
    return render_template('blog/home.html')
