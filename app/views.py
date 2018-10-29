from flask import Blueprint

static = Blueprint('static', __name__)


@static.route('/')
def index():
    return 'Static index'
