'''
    app.misc.views
    ~~~~~~~~~~~~~~

    End points for miscellaneous applications.
'''
from flask import Blueprint, render_template, request
from app.misc.forms import DasTraderHotkeyGeneratorForm
from app.modules.das_trader_hotkey_generator import generate_hotkeys
from app.misc.models.das_trader import DasTrader

misc = Blueprint('misc', __name__)


@misc.route('/das-trader-hotkey-generator', methods=['GET', 'POST'])
def das_trader_hotkey_generator():
    hotkeys = None
    form = DasTraderHotkeyGeneratorForm()
    if form.validate_on_submit():
        hotkeys = generate_hotkeys(
            risk=form.risk.data,
            route=form.route.data,
            sc_long_key=form.long_key.data,
            sc_short_key=form.short_key.data)
        dt = DasTrader(ip_address=request.remote_addr)
        dt.commit()
    return render_template('misc/das-trader-hotkey-generator/index.html',
                           form=form, hotkeys=hotkeys)
