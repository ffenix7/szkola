from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired
import secrets
import json

#funkcje do obsługi pliku

def load_users():
    try:
        with open('users.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def save_users(users):
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(users,f, indent=4)

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
bootstrap = Bootstrap(app)

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj się')

class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zarejestruj się')

@app.route('/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        users = load_users()
        user = None
        for u in users:
            if u['email'] == login_form.email.data and u['password'] == login.foorm.password.data:
                user = u
                break
        if user:
            session['user'] = login_form.email.data
            flash('Zalogowano pomyślnie!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Nieprawidłowa nazwa użytkownika lub hasło.', 'danger')
    return render_template(template_name_or_list='login.html',title="logowanie", login_form=login_form)

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Wylogowano pomyślnie.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    user = session.get('user')
    if not user:
        flash('Proszę się zalogować, aby uzyskać dostęp do panelu użytkownika.', 'warning')
        return redirect(url_for('login'))
    return render_template(template_name_or_list='dashboard.html', title="Panel użytkownika")

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        users = load_users()

        if any(user['email'] == register_form.email.data for user in users):
            flash('Użytkownik o podanym emailu już istnieje.', 'danger')
            return redirect(url_for('register'))
        
        # for user in users:
        #     if user['password'] == register_form.password.data:
        #         flash(f'Użytkownik o podanym haśle już istnieje. Czy twój mail to {user['email']}', 'danger')
        #         return redirect(url_for('register'))
        
        new_user = {
            'email': register_form.email.data,
            'password': register_form.password.data
        }

        users.append(new_user)
        save_users(users)
        flash('Rejestracja zakończona pomyślnie! Możesz się teraz zalogować.', 'success')
        return redirect(url_for('login'))
    return render_template(template_name_or_list='register.html', title="Rejestracja", register_form=register_form)


if __name__ == '__main__':
    app.run(debug=True)
