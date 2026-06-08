from flask import Blueprint, current_app, flash, redirect, url_for, render_template, request, abort
from flask_login import login_required, current_user, login_user, logout_user
from extensions import db
from models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.get('/login')
def login_get():
    if current_user.is_authenticated:
        return redirect(url_for('drive.dashboard'))
    return render_template('auth_login.html', title='Logowanie')


@auth_bp.post('/login')
def login_post():
    if current_user.is_authenticated:
        return redirect(url_for('drive.dashboard'))
    email = (request.form.get('email') or '').strip().lower()
    password = request.form.get('password') or ''
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        flash('Błędny email lub hasło', 'danger')
        return redirect(url_for('auth.login_get'))
    login_user(user)
    flash('Zalogowano poprawnie', 'success')
    return redirect(url_for('drive.dashboard'))


@auth_bp.post('/logout')
@login_required
def logout():
    logout_user()
    flash('Wylogowano', 'success')
    return redirect(url_for('auth.login_get'))


@auth_bp.get('/setup')
def setup_get():
    if db.session.query(User.id).limit(1).first() is not None:
        abort(404)
    setup_token = (request.args.get('token') or '').strip()
    if not current_app.config.get('SETUP_TOKEN'):
        abort(404)
    if setup_token != current_app.config.get('SETUP_TOKEN'):
        abort(403)
    return render_template('setup_admin.html', title='Ustawienia')


@auth_bp.post('/setup')
def setup_post():
    if db.session.query(User.id).limit(1).first() is not None:
        abort(404)
    setup_token = (request.args.get('token') or '').strip()
    if not current_app.config.get('SETUP_TOKEN'):
        abort(404)
    if setup_token != current_app.config.get('SETUP_TOKEN'):
        abort(403)
    email = (request.form.get('email') or '').strip().lower()
    password = request.form.get('password') or ''
    if not email or not password:
        flash('Email i hasło są wymagane', 'danger')
        return redirect(url_for('auth.setup_get', token=setup_token))
    user = User(email=email, role='admin', quota_bytes=100 * 1024 * 1024 * 1024)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    flash('Utworzono konto administratora', 'success')
    return redirect(url_for('drive.dashboard'))