import datetime
from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, Optional, URL

CURRENT_YEAR = datetime.date.today().year

class BookForm(FlaskForm):
    title = StringField("Tytuł", validators=[DataRequired(), Length(max=100)])
    author = StringField("Autor", validators=[DataRequired(), Length(max=100)])
    genre = StringField("Gatunek", validators=[DataRequired(), Length(max=50)])
    published_year = IntegerField(
        "Rok wydania",
        validators=[
            DataRequired(),
            NumberRange(min=0, max=CURRENT_YEAR, message="Rok wydania musi być realistyczny"),
        ],
    )
    cover_url = StringField(
        "Adres okładki",
        validators=[Optional(), URL(require_tld=False, message="Podaj poprawny adres URL"), Length(max=255)],
    )
    description = TextAreaField("Opis", validators=[DataRequired()])
    submit = SubmitField("Zapisz")

class RegistrationForm(FlaskForm):
    user_first_name = StringField("Imię", validators=[DataRequired(), Length(max=20)])
    user_last_name = StringField("Nazwisko", validators=[DataRequired(), Length(max=30)])
    user_email = StringField("E-mail", validators=[DataRequired(), Email(), Length(max=50)])
    password = PasswordField("Hasło", validators=[DataRequired(), Length(min=6, max=32)])
    confirm_password = PasswordField(
        "Powtórz hasło", validators=[DataRequired(), EqualTo("password", message="Hasła muszą być identyczne.")]
    )
    submit = SubmitField("Załóż konto")

class LoginForm(FlaskForm):
    user_email = StringField("E-mail", validators=[DataRequired(), Email(), Length(max=50)])
    password = PasswordField("Hasło", validators=[DataRequired()])
    submit = SubmitField("Zaloguj")