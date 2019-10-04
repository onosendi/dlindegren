'''
    app.misc.models.das_trader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
from datetime import datetime
from app.extensions import db
from app.models.mixins import BaseControl


class MiscDasTrader(BaseControl, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    ip_address = db.Column(db.VARCHAR(39), nullable=False)
