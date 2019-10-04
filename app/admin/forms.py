'''
    app.admin.forms
    ~~~~~~~~~~~~~~~
'''
import re
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    StringField, BooleanField, PasswordField, SubmitField)
from wtforms.validators import (
    DataRequired, Email, Length, EqualTo, ValidationError)


class LoginForm(FlaskForm):
    email = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')


class FirstTimeForm(FlaskForm):
    ''' Register first time administrator.

    ..Note: No need to validate if email already exists in the database, since
    the endpoint will turn you away if there are any existing users.
    '''
    username = StringField('Username',
                           validators=[DataRequired(), Length(max=35)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=8, max=32)])
    password2 = PasswordField(
        'Repeat password', validators=[DataRequired(),
                                       EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        # Make sure ``username``:
        # - Has alphanumeric / underscore
        # - Starts with alpha
        # - Doesn't start or end with an underscore
        regex = '^[a-zA-Z][a-zA-Z1-9_]*[a-zA-Z0-9]+$'
        if not re.match(regex, username.data):
            raise ValidationError('Invalid username. Example: john_doe13')
