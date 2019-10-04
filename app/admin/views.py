'''
    app.admin.views
    ~~~~~~~~~~~~~~~

    End points for admin.
'''
from werkzeug.urls import url_parse
from flask import Blueprint, render_template, redirect, url_for, flash, request
from sqlalchemy import func
from flask_login import current_user, login_user, logout_user, login_required
from app.admin.models import AdminUser
from app.admin.forms import LoginForm

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@login_required
def index():
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.home'))
    form = LoginForm()
    if form.validate_on_submit():
        login = func.lower(form.email.data)
        user_by_email = AdminUser.query.filter(
            func.lower(AdminUser.email) == func.lower(login)).first()
        user_by_username = AdminUser.query.filter(
            func.lower(AdminUser.username) == func.lower(login)).first()
        user = user_by_email if user_by_email else user_by_username
        if (user is None or not user.check_password(form.password.data) or not
                user.active):
            flash('Invalid email or password.')
            return redirect(url_for('admin.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('admin.index')
        return redirect(next_page)
    return render_template('admin/login.html', form=form)


@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admin.login'))
