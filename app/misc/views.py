from flask import Blueprint, render_template

misc = Blueprint('misc', __name__)


@misc.route('/das-trader-hotkey-generator')
def das_trader_hotkey_generator():
    return render_template('misc/das-trader-hotkey-generator/index.html') 
