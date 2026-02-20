from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired

class AddProductForm(FlaskForm):
    symbol = StringField('Symbol', validators=[DataRequired()])
    item_name = StringField('Nazwa produktu', validators=[DataRequired()])
    quantity = IntegerField('Ilość', validators=[DataRequired()])
    price_pln = FloatField('Cena (PLN)', validators=[DataRequired()])
    category = StringField('Kategoria', validators=[DataRequired()])
    brand = StringField('Marka', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    weight_kg = FloatField('Waga (kg)', validators=[DataRequired()])
    submit = SubmitField('Dodaj produkt')

class EditProductForm(FlaskForm):
    symbol = StringField('Symbol', validators=[DataRequired()])
    item_name = StringField('Nazwa produktu', validators=[DataRequired()])
    quantity = IntegerField('Ilość', validators=[DataRequired()])
    price_pln = FloatField('Cena (PLN)', validators=[DataRequired()])
    category = StringField('Kategoria', validators=[DataRequired()])
    brand = StringField('Marka', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    weight_kg = FloatField('Waga (kg)', validators=[DataRequired()])
    submit = SubmitField('Zapisz zmiany')