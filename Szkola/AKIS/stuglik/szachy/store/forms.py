from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, NumberRange, Optional, Email


class TournamentForm(FlaskForm):
    name = StringField('Nazwa turnieju', validators=[DataRequired()])
    category = StringField('Kategoria', validators=[DataRequired()], default='Open')
    selection_mode = SelectField(
        'Uczestnicy',
        choices=[('all', 'Wszyscy zawodnicy'), ('selected', 'Tylko wybrani')],
        validators=[DataRequired()],
        default='all'
    )
    pairing_method = SelectField(
        'Parowanie',
        choices=[('name', 'Nazwisko'), ('age', 'Wiek'), ('ranking', 'Ranking')],
        validators=[DataRequired()],
        default='ranking'
    )
    submit = SubmitField('Zapisz')


class PlayerForm(FlaskForm):
    first_name = StringField('Imię', validators=[DataRequired()])
    last_name = StringField('Nazwisko', validators=[DataRequired()])
    email = StringField('Email', validators=[Optional(), Email()])
    age = IntegerField('Wiek', validators=[DataRequired(), NumberRange(min=5, max=120)])
    ranking = IntegerField('Ranking', validators=[DataRequired(), NumberRange(min=0, max=4000)])
    gender = SelectField(
        'Kategoria',
        choices=[('O', 'Open'), ('K', 'Kobiety'), ('M', 'Mężczyźni')],
        default='O'
    )
    submit = SubmitField('Dodaj zawodnika')


class ParticipantSelectionForm(FlaskForm):
    player_ids = SelectMultipleField('Wybierz zawodników', coerce=int)
    submit = SubmitField('Zapisz uczestników')