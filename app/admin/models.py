'''
    app.blog.models
    ~~~~~~~~~~~~~~~

    Blog models.
'''
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.extensions import db, login
from app.base_models import BaseModel, BaseControl


class AdminUser(UserMixin, db.Model, BaseModel, BaseControl):
    username = db.Column(db.String(35), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


def register_user(username, email, password):
    user = AdminUser(username=username, email=email)
    user.set_password(password)
    user.commit()
    return user


@login.user_loader
def load_user(id):
    ''' For :mod:flask_login. '''
    return User.query.get(int(id))
