from . import shop_bp
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models import Inventory, CartItem

@shop_bp.route('/shop')
@login_required
def index():
    products = Inventory.query.all()
    return render_template('shop/index.html', products=products, title='Shop')

@shop_bp.route('/shop/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    product = Inventory.query.get_or_404(product_id)

    if product.quantity < 1:
        flash('Sorry, this product is out of stock.', 'danger')
        return redirect(url_for('shop.index'))

    item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()

    if item:
        item.quantity += 1
    else:
        item = CartItem(user_id=current_user.id, product_id=product_id, quantity=1)
        db.session.add(item)
    db.session.commit()
    return redirect(url_for('shop.cart'))

@shop_bp.route('/shop/cart')
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price_pln * item.quantity for item in cart_items)
    return render_template('shop/cart.html', cart_items=cart_items, total=total, title='Your Cart')