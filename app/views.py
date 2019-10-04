'''
    app.views
    ~~~~~~~~~

    End points for static pages.
'''
from flask import Blueprint, render_template

static_view = Blueprint('static_view', __name__)


@static_view.route('/')
def index():
    return render_template('index.html')
