'''
    app.views
    ~~~~~~~~~

    End points for static pages.
'''
from flask import Blueprint, render_template

frontend = Blueprint('static_view', __name__)


@frontend.route('/')
def index():
    return render_template('static_view/index.html')
