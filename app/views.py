'''
    app.views
    ~~~~~~~~~

    End points for static pages.
'''
from flask import Blueprint, render_template

static = Blueprint('static', __name__)


@static.route('/')
def home():
    return render_template('home.html')
