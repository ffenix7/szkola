from flask_login import UserMixin
from extensions import db

class Users(db.Model, UserMixin):
    id       = db.Column(db.Integer, primary_key=True)
    email    = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<User {self.email}>'
    
class Inventory(db.Model):
    # __bind_key__ = 'inventory'
    
    id                  = db.Column(db.Integer, primary_key=True)
    symbol              = db.Column(db.String(50))
    name                = db.Column(db.String(200))
    category            = db.Column(db.String(100))
    brand               = db.Column(db.String(100))
    model               = db.Column(db.String(100))
    quantity            = db.Column(db.Integer)
    weight_kg           = db.Column(db.Float)
    price_pln           = db.Column(db.Float)
    inventory_value_pln = db.Column(db.Float)

class CartItem(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    user_id   = db.Column(db.Integer, nullable=False)
    product_id   = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    quantity  = db.Column(db.Integer, nullable=False, default=1)
    product = db.relationship('Inventory')

class Order(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    created_at  = db.Column(db.DateTime, server_default=db.func.now())

class OrderItem(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    order_id    = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id  = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    quantity    = db.Column(db.Integer, nullable=False)
    price_pln   = db.Column(db.Float, nullable=False)
    
    order = db.relationship('Order')