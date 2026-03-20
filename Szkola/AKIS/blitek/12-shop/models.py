from flask_login import UserMixin
from extentions import db

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"
    
class Inventory(db.Model):
    __bind_key__ = 'inventory'
    id                      = db.Column(db.Integer, primary_key=True)
    item_name               = db.Column(db.String(50), nullable=False)
    symbol                  = db.Column(db.String(10), nullable=False)
    model                   = db.Column(db.String(50), nullable=False)
    brand                   = db.Column(db.String(50), nullable=False)
    category                = db.Column(db.String(50), nullable=False)
    quantity                = db.Column(db.Integer, nullable=False)
    price_pln               = db.Column(db.Float, nullable=False)
    weight_kg               = db.Column(db.Float, nullable=False)
    inventory_value_pln     = db.Column(db.Float, nullable=False)