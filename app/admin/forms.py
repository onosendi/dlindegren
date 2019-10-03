'''
    app.admin.forms
    ~~~~~~~~~~~~~~~

    Admin forms.
'''
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    StringField, BooleanField, PasswordField, SubmitField)
from wtforms.validators import (
    DataRequired)


class LoginForm(FlaskForm):
    email = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')
