from . import shop_bp
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models import Inventory, CartItem, Order, OrderItem

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

@shop_bp.route('/shop/remove_from_cart/<int:product_id>')
@login_required
def remove_from_cart(product_id):
    item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('shop.cart'))

@shop_bp.route('/shop/cart')
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price_pln * item.quantity for item in cart_items)
    return render_template('shop/cart.html', cart_items=cart_items, total_price=total, title='Your Cart')

@shop_bp.route('/checkout')
@login_required
def checkout():
    items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not items:
        flash('Your cart is empty.', 'warning')
        return redirect(url_for('shop.cart'))
        
    total = 0
    order = Order(user_id=current_user.id, total_price=0)
    db.session.add(order)
    db.session.flush() 

    for item in items:
        if item.product.quantity < item.quantity:
            flash(f'Sorry, not enough stock for {item.product.name}.', 'danger')
            db.session.rollback()
            return redirect(url_for('shop.cart'))
        
        item.product.quantity -= item.quantity
        subtotal = item.product.price_pln * item.quantity
        total += subtotal
        order_item = OrderItem(order_id=order.id, product_id=item.product_id, quantity=item.quantity, price_pln=subtotal)
        db.session.add(order_item)
    
    for item in items:
        db.session.delete(item)

    db.session.commit()
    return redirect(url_for('shop.index'))

@shop_bp.route('/orders')
@login_required
def orders():
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    order_ids = [order.id for order in orders]
    items = []
    for order_id in order_ids:
        items = (
            OrderItem.query.filter_by(order_id=order_id)
            .order_by(OrderItem.order_id.desc(), OrderItem.id.asc())
            .all()
        )

    product_ids = sorted({item.product_id for item in items})
    products = []
    if product_ids:
        products = Inventory.query.filter(Inventory.id.in_(product_ids)).all()
    products_by_id = {product.id: product for product in products}
    
    items_by_order = {order_id: [] for order_id in order_ids}
    for item in items:
        items_by_order.setdefault(item.order_id, []).append(item)
    
    return render_template(
        'shop/orders.html',
        orders=orders,
        items_by_order=items_by_order,
        products_by_id=products_by_id,
    )