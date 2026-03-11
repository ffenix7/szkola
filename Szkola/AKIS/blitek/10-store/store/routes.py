from flask import render_template, redirect, request, url_for, flash, Response, current_app
from flask_login import login_required
from extensions import db
from models import Inventory
from . import store_bp
from .forms import AddProductForm
import pandas as pd
from io import StringIO
from sqlalchemy import func, asc, desc

@store_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    add_product_form = AddProductForm()
    page = request.args.get('page', 1, int)
    search = request.args.get('search', '').strip()
    order = request.args.get('order', 'id').strip().lower()
    direction = request.args.get('direction', 'asc').strip().lower()
    query = Inventory.query
    
    if search:
        query = query.filter(
            Inventory.name.ilike(f'%{search}')     |
            Inventory.symbol.ilike(f"%{search}")   |
            Inventory.brand.ilike(f"%{search}")    |
            Inventory.model.ilike(f"%{search}")    |
            Inventory.category.ilike(f"%{search}")
        )
        
    col = getattr(Inventory, order)
    if direction == 'desc': col = desc(col)
    else: col = asc(col)
        
    pagination = query.order_by(col).paginate(page=page, per_page=20)
    records = pagination.items
    
    return render_template(
        'store/index.html',
        title='Magazyn',
        records=records,
        pagination=pagination,
        search=search,
        order=order,
        direction=direction,
        add_product_form=add_product_form
    )

@store_bp.route('/import', methods=['GET', 'POST']) # type: ignore
@login_required
def import_data():
    file = request.files.get('file')
    
    if not file:
        flash('Nie wybrano pliku', 'error')
        return redirect(url_for('store.index'))
    
    try:
        df = pd.read_csv(file) # type: ignore
    except Exception as e:
        flash(f"Błąd wczytywania pliku: {e}", 'danger')
        return redirect(url_for('store.index'))
    
    db.session.query(Inventory).delete()
    
    for _, row in df.iterrows():
        item = Inventory(
            id                  = int(row['id']),                   # type: ignore
            symbol              = row['symbol'],                      # type: ignore
            name                = row['name'],                        # type: ignore
            category            = row['category'],                    # type: ignore
            brand               = row['brand'],                       # type: ignore
            model               = row['model'],                       # type: ignore
            quantity            = int(row['quantity']),             # type: ignore
            weight_kg           = float(row['weight_kg']),          # type: ignore
            price_pln           = float(row['price_pln']),          # type: ignore
            inventory_value_pln = float(row['inventory_value_pln']) # type: ignore
        )
        
        db.session.add(item)
        
    db.session.commit()
    flash('Dane zostały zapisane poprawnie', 'success')
    return redirect(url_for('store.index'))

@store_bp.route('/export', methods=['GET']) # type: ignore
@login_required
def export_data():
    query = "SELECT * FROM inventory ORDER BY id"
    
    engine = db.get_engine(current_app, bind='inventory') # type: ignore
    df = pd.read_sql(query, engine)
    
    output = StringIO()
    df.to_csv(output, index=False)
    
    response = Response(output.getvalue(), mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=inventory_export.csv'
    return response

@store_bp.route('/add-product', methods=['GET', 'POST']) # type: ignore
@login_required
def add_product():
    if request.method == 'POST':
        symbol              = request.form.get('symbol')
        name                = request.form.get('name')
        category            = request.form.get('category')
        brand               = request.form.get('brand')
        model               = request.form.get('model')
        quantity            = request.form.get('quantity' , type=int)
        weight_kg           = request.form.get('weight_kg', type=float)
        price_pln           = request.form.get('price_pln', type=float)
        inventory_value_pln = round(quantity * price_pln, 2) if quantity and price_pln else 0

        new_item = Inventory(
            symbol              = symbol,              # type: ignore
            name                = name,                # type: ignore
            category            = category,            # type: ignore
            brand               = brand,               # type: ignore    
            model               = model,               # type: ignore
            quantity            = quantity,            # type: ignore
            weight_kg           = weight_kg,           # type: ignore    
            price_pln           = price_pln,           # type: ignore
            inventory_value_pln = inventory_value_pln  # type: ignore
        )
        
        db.session.add(new_item)
        db.session.commit()
        
        flash('Produkt został dodany', 'success')
        return redirect(url_for('store.index'))
    
@store_bp.route('/modify-product', methods=["GET", "POST"]) # type: ignore
@login_required
def modify_product():
    if request.method == 'POST':
        item = Inventory.query.get(request.args.get('id'))
        item.symbol              = request.form.get('symbol')                # type: ignore
        item.name                = request.form.get('name')                  # type: ignore
        item.category            = request.form.get('category')              # type: ignore
        item.brand               = request.form.get('brand')                 # type: ignore
        item.model               = request.form.get('model')                 # type: ignore
        item.quantity            = request.form.get('quantity' , type=int)   # type: ignore
        item.weight_kg           = request.form.get('weight_kg', type=float) # type: ignore
        item.price_pln           = request.form.get('price_pln', type=float) # type: ignore
        item.inventory_value_pln = round(item.quantity * item.price_pln, 2) if item.quantity and item.price_pln else 0 # type: ignore

        db.session.commit()
        flash('Produkt został zmodyfikowany', 'success')
        return redirect(url_for('store.index'))
    
@store_bp.route('/delete-product', methods=['GET', 'POST']) # type: ignore
@login_required
def delete_product():
    if request.method == 'POST':
        db.session.query(Inventory).filter_by(id=request.args.get('id')).delete()
        db.session.commit()
        flash('Produkt został usunięty', 'success')
        return redirect(url_for('store.index'))