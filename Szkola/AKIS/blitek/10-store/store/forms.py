from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired

class AddProductForm(FlaskForm):
    symbol    = StringField ('Symbol'          , [DataRequired()])
    name      = StringField ('Nazwa'           , [DataRequired()])
    category  = StringField ('Kategoria'       , [DataRequired()])
    brand     = StringField ('Producent'       , [DataRequired()])
    model     = StringField ('Model'           , [DataRequired()])
    quantity  = IntegerField('Ilość'           , [DataRequired()])
    weight_kg = FloatField  ('Wgaga (kg)'      , [DataRequired()])
    weight_kg = FloatField  ('Waga (kg)'       , [DataRequired()])
    price_pln = FloatField  ('Cena jednostkowa', [DataRequired()])
    submit    = SubmitField ('Dodaj')