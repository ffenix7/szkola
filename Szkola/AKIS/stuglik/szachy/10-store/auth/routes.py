from flask import render_template, request, redirect, url_for, session, flash, Blueprint
from .forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user, login_required
from extentions import db, bcrypt
from models import Users

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Users.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=True)
            session['user'] = user.email
            flash('Zalogowano pomyślnie!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('auth.dashboard'))
        else:
            flash('Nieprawidłowa nazwa użytkownika lub hasło.', 'danger')
    return render_template(template_name_or_list='auth/login.html',title="logowanie", login_form=login_form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    session.pop('user', None)
    flash('Wylogowano pomyślnie.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    user = session.get('user')
    if not user:
        flash('Proszę się zalogować, aby uzyskać dostęp do panelu użytkownika.', 'warning')
        return redirect(url_for('auth.login'))
    return render_template(template_name_or_list='auth/dashboard.html', title="Panel użytkownika")

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        try:
            hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')

            user = Users(email=register_form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Rejestracja zakończona pomyślnie! Możesz się teraz zalogować.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash('Błąd podczas rejestracji! .', 'danger')
    return render_template(template_name_or_list='auth/register.html', title="Rejestracja", register_form=register_form)
