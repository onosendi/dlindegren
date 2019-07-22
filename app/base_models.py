'''
    app.base_models
    ~~~~~~~~~~~~~~~

    Mixins for SQLAlchemy.
'''
from app.extensions import db


class BaseControl:
    def commit(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as E:
            db.session.rollback()
            raise E
