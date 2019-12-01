'''
    app.views
    ~~~~~~~~~

    End points for static pages.
'''
from flask import Blueprint, render_template, flash

dlindegren = Blueprint('static_view', __name__)


@dlindegren.route('/')
def index():
    return render_template('dlindegren/index.html')
