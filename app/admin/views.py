'''
    app.admin.views
    ~~~~~~~~~~~~~~~

    End points for admin.
'''
import re
import urllib.parse
from werkzeug.urls import url_parse
from flask import (Blueprint, render_template, redirect, url_for, flash,
                   request, jsonify, abort)
from sqlalchemy import func
from flask_login import current_user, login_user, logout_user, login_required
from app.admin.models import AdminUser, register_user
from app.blog.models import BlogArticle
from app.admin.forms import LoginForm, FirstTimeForm

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/blog')
@login_required
def blog():
    articles = BlogArticle.query.filter_by(active=True).\
        order_by(BlogArticle.created.desc()).all()
    return render_template('admin/blog.html', articles=articles)


@admin.route('/blog/<int:article_id>', methods=['POST', 'PUT', 'DELETE'])
def blog_control(article_id):
    article = BlogArticle.query.filter_by(id=article_id).first()
    if not article:
        abort(404)
    article_dict = {
        'article_id': article.id,
        'article_name': article.article_name,
        'file_name': article.file_name}
    if request.method == 'PUT':
        article_name = request.json.get('article_name')
        file_name = re.sub(r'\W+', '-', article_name)
        article.article_name = article_name
        article.file_name = file_name
        article.commit()
    if request.method == 'DELETE':
        article.delete()
        article.commit()
    return jsonify(article_dict)


@admin.route('/')
@login_required
def index():
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
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


@admin.route('first-time', methods=['GET', 'POST'])
def first_time():
    if AdminUser.query.count() > 0:
        return redirect(url_for('admin.login'))
    form = FirstTimeForm()
    if form.validate_on_submit():
        user = register_user(form.username.data, form.email.data,
                             form.password.data)
        login_user(user)
        return redirect(url_for('admin.index'))
    return render_template('admin/first-time.html', form=form)


@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admin.login'))
