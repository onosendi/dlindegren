'''
    app.util.views
    ~~~~~~~~~~~~~~
'''
from flask import jsonify


def json_error(error):
    return jsonify({'status': False,
                    'error': error})
