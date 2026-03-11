from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from extensions import db, bcrypt
from models import Users

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Users.query.filter_by(email=login_form.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            flash('Zalogowano poprawnie', 'success')
            return redirect(url_for('auth.dashboard'))
        
        flash('Nieprawidłowe dane logowania', 'danger')
    
    return render_template('auth/login.html', title='Login', login_form=login_form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        try:
            hashed_passowrd = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
            user = Users(email=register_form.email.data, password=hashed_passowrd) # type: ignore
            
            db.session.add(user)
            db.session.commit()
            
            flash('Konto utworzone poprawnie', 'success')
            return redirect(url_for('auth.login'))
        except Exception:
            flash('Błąd', 'error')
            
    return render_template('auth/register.html', title='Register', register_form=register_form)

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('auth/dashboard.html', title='Dashboard')

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Wylogowano poprawnie', 'success')
    return redirect(url_for('auth.login'))