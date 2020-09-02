import os

from flask import Flask, render_template

from config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)
if os.environ['FLASK_ENV'] == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)


@app.route('/')
def index():
    return render_template('index.jinja')
