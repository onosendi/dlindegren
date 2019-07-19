from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class DasTraderHotkeyGeneratorForm(FlaskForm):
    risk = StringField('Risk')
    route = StringField('Route')
    long_key = StringField('Long key(s)')
    short_key = StringField('Short key(s)')
    submit = SubmitField('Generator Hotkeys')
