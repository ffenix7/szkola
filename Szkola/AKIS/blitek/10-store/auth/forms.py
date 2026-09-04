from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class EmailForm(FlaskForm):
    email = EmailField('Login', validators=[DataRequired()])
    password = PasswordField('Hasło:', validators=[DataRequired()])

class LoginForm(EmailForm):
    submit = SubmitField('Zaloguj się')
    
class RegistrationForm(EmailForm):
    submit = SubmitField('Zarejestruj się')