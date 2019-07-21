from flask import Blueprint, render_template, redirect, url_for
from app.misc.forms import DasTraderHotkeyGeneratorForm
from app.modules.das_trader_hotkey_generator import generate_hotkeys

misc = Blueprint('misc', __name__)


@misc.route('/das-trader-hotkey-generator', methods=['GET', 'POST'])
def das_trader_hotkey_generator():
    hotkeys = None
    form = DasTraderHotkeyGeneratorForm()
    if form.validate_on_submit():
        hotkeys = generate_hotkeys(
            risk = form.risk.data,
            route = form.route.data,
            sc_long_key=form.long_key.data,
            sc_short_key=form.short_key.data)
    return render_template('misc/das-trader-hotkey-generator/index.html',
                           form=form, hotkeys=hotkeys)