from . import shop_bp
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from extensions import db
from models import Inventory, CartItem, Order, OrderItem

@shop_bp.route('/')
@login_required
def index():
    products = Inventory.query.all()
    return render_template('shop/index.html', products=products, title='Shop')

@shop_bp.route('/add_to_cart/<int:product_id>')
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
    flash('Produkt dodany do koszyka.', 'success')
    return redirect(url_for('shop.cart'))

@shop_bp.route('/remove_from_cart/<int:product_id>')
@login_required
def remove_from_cart(product_id):
    item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        flash('Produkt usunięty z koszyka.', 'info')
    return redirect(url_for('shop.cart'))

@shop_bp.route('/cart')
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price_pln * item.quantity for item in cart_items)
    return render_template('shop/cart.html', cart_items=cart_items, total_price=total, title='Your Cart')

@shop_bp.route('/update_cart/<int:product_id>', methods=['POST'])
@login_required
def update_cart(product_id):
    item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first_or_404()
    quantity = request.form.get('quantity', type=int)

    if quantity is None or quantity < 1:
        flash('Nieprawidłowa ilość produktu.', 'warning')
        return redirect(url_for('shop.cart'))

    max_available = item.product.quantity
    if quantity > max_available:
        flash('Wybrana ilość przekracza stan magazynowy.', 'warning')
        return redirect(url_for('shop.cart'))

    item.quantity = quantity
    db.session.commit()
    flash('Koszyk został zaktualizowany.', 'success')
    return redirect(url_for('shop.cart'))

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
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price_pln=subtotal,
        )
        db.session.add(order_item)
    
    for item in items:
        db.session.delete(item)

    order.total_price = total
    db.session.commit()
    flash('Zamówienie zostało złożone.', 'success')
    return redirect(url_for('shop.index'))

@shop_bp.route('/orders')
@login_required
def orders():
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    order_ids = [order.id for order in orders]
    items = []
    if order_ids:
        items = (
            OrderItem.query.filter(OrderItem.order_id.in_(order_ids))
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

    # Backfill legacy orders that were created with total_price=0.
    updated = False
    for order in orders:
        if (order.total_price is None or float(order.total_price) == 0.0) and items_by_order.get(order.id):
            order.total_price = float(sum(order_item.price_pln for order_item in items_by_order[order.id]))
            updated = True

    if updated:
        db.session.commit()
    
    return render_template(
        'shop/orders.html',
        title='Orders',
        orders=orders,
        items_by_order=items_by_order,
        products_by_id=products_by_id,
    )