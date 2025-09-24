from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
import secrets

#przykładowe dane logowania

VALID_USERNAME = "admin"
VALID_PASSWORD = "zaq12wsx"

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
bootstrap = Bootstrap(app)

class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj się')

@app.route('/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        if login_form.username.data == VALID_USERNAME and login_form.password.data == VALID_PASSWORD:
            session['user'] = login_form.username.data
            flash('Zalogowano pomyślnie!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Nieprawidłowa nazwa użytkownika lub hasło.', 'danger')
    return render_template(template_name_or_list='index.html',title="logowanie", login_form=login_form)

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
if __name__ == '__main__':
    app.run(debug=True)