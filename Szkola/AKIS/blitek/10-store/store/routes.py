from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from extentions import db
from models import Inventory
from . import store_bp
import pandas as pd
from . forms import AddProductForm, EditProductForm

# @store_bp.route('/')
# @login_required
# def index():
#     records = Inventory.query.all()
#     return render_template('store/index.html', title='Store Inventory', records=records)

@store_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    add_product_form = AddProductForm()
    edit_product_form = EditProductForm()
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    query = Inventory.query
    if search:
        query = query.filter(
            Inventory.item_name.ilike(f'%{search}%') |
            Inventory.symbol.ilike(f'%{search}%') |
            Inventory.category.ilike(f'%{search}%') |
            Inventory.brand.ilike(f'%{search}%') |
            Inventory.model.ilike(f'%{search}%')
        )

    pagination= query.order_by(Inventory.id).paginate(page=page, per_page=10)
    records = pagination.items
    return render_template('store/index.html', title='Store Inventory', records=records, pagination=pagination, search=search, add_product_form=add_product_form, edit_product_form=edit_product_form)


@store_bp.route('/import', methods=['GET', 'POST'])
@login_required
def import_data():
    file = request.files.get('file')
    if not file:
        flash("Nie wybrano pliku!", category='danger')
        return redirect(url_for('store.index'))
    
    try:
        df = pd.read_csv(file)
    except Exception as err:
        flash(f"Błąd wczytywania pliku {err}", category="danger")
        return redirect(url_for('store.index'))
    
    db.session.query(Inventory).delete()

    #dodanie rekordów
    for _, row in df.iterrows():
        item = Inventory(
            id=int(row['id']),
            symbol=row['symbol'],
            item_name=row['item_name'],
            quantity=int(row['quantity']),
            price_pln=float(row['price_pln']),
            category=row['category'],
            brand = row['brand'],
            model = row['model'],
            weight_kg = row['weight_kg'],
            inventory_value_pln = int(row['quantity']) * float(row['price_pln'])
        )
        db.session.add(item)
    db.session.commit()
    flash("Dane zostały zaimportowane pomyślnie!", category='success')
    return redirect(url_for('store.index'))

@store_bp.route('/add_product', methods=['POST'])
@login_required
def add_product():
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        item_name = request.form.get('item_name')
        quantity = request.form.get('quantity' ,type=int)
        price_pln = request.form.get('price_pln', type=float)
        category = request.form.get('category')
        brand = request.form.get('brand')
        model = request.form.get('model')
        weight_kg = request.form.get('weight_kg', type=float)

        inventory_value_pln = int(quantity) * float(price_pln) if quantity and price_pln else 0

        new_product = Inventory(
            symbol=symbol,
            item_name=item_name,
            quantity=int(quantity),
            price_pln=float(price_pln),
            category=category,
            brand=brand,
            model=model,
            weight_kg=float(weight_kg),
            inventory_value_pln=inventory_value_pln
        )
        db.session.add(new_product)
        db.session.commit()
        flash("Produkt został dodany pomyślnie!", category='success')
    return redirect(url_for('store.index'))

@login_required
@store_bp.route('/edit_product/<int:product_id>', methods=['POST'])
def edit_product(product_id):
    product = Inventory.query.get(product_id)

    product.symbol = request.form.get('symbol')
    product.item_name = request.form.get('item_name')
    product.quantity = int(request.form.get('quantity', product.quantity))
    product.price_pln = float(request.form.get('price_pln', product.price_pln))
    product.category = request.form.get('category')
    product.brand = request.form.get('brand')
    product.model = request.form.get('model')
    product.weight_kg = float(request.form.get('weight_kg', product.weight_kg))

    product.inventory_value_pln = product.quantity * product.price_pln

    db.session.commit()
    flash("Produkt został zaktualizowany pomyślnie!", category='success')
    return redirect(url_for('store.index'))

@login_required
@store_bp.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Inventory.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    flash("Produkt został usunięty pomyślnie!", category='success')
    return redirect(url_for('store.index'))