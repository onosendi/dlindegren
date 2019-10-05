'''
    app.views
    ~~~~~~~~~

    End points for static pages.
'''
from flask import Blueprint, render_template, flash

frontend = Blueprint('static_view', __name__)


@frontend.route('/')
def index():
    return render_template('frontend/index.html')
