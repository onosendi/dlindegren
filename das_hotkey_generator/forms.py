from django.forms import (
    Form,
    CharField,
    BooleanField,
)


class DasHotkeyGeneratorForm(Form):
    risk = CharField(label='Risk (dollars)', required=False)
    route = CharField(label='Route', required=False)
    long_key = CharField(label='Long key(s)', required=False)
    short_key = CharField(label='Short key(s)', required=False)
    default_hotkeys = BooleanField(label='Include defaults', required=False)
