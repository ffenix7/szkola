from flask import render_template, request, redirect, url_for, session, flash, Blueprint
from .forms import LoginForm, RegisterForm, load_users, save_users

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        users = load_users()
        user = None
        for u in users:
            if u['email'] == login_form.email.data and u['password'] == login_form.password.data:
                user = u
                break
        if user:
            session['user'] = login_form.email.data
            flash('Zalogowano pomyślnie!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Nieprawidłowa nazwa użytkownika lub hasło.', 'danger')
    return render_template(template_name_or_list='login.html',title="logowanie", login_form=login_form)

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Wylogowano pomyślnie.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    user = session.get('user')
    if not user:
        flash('Proszę się zalogować, aby uzyskać dostęp do panelu użytkownika.', 'warning')
        return redirect(url_for('login'))
    return render_template(template_name_or_list='dashboard.html', title="Panel użytkownika")

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        users = load_users()

        if any(user['email'] == register_form.email.data for user in users):
            flash('Użytkownik o podanym emailu już istnieje.', 'danger')
            return redirect(url_for('register'))

        new_user = {
            'email': register_form.email.data,
            'password': register_form.password.data
        }

        users.append(new_user)
        save_users(users)
        flash('Rejestracja zakończona pomyślnie! Możesz się teraz zalogować.', 'success')
        return redirect(url_for('login'))
    return render_template(template_name_or_list='register.html', title="Rejestracja", register_form=register_form)
