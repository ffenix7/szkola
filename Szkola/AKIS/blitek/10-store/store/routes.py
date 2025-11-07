from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from extentions import db
from models import Inventory
from . import store_bp
import pandas as pd

# @store_bp.route('/')
# @login_required
# def index():
#     records = Inventory.query.all()
#     return render_template('store/index.html', title='Store Inventory', records=records)

@store_bp.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    pagination= Inventory.query.order_by(Inventory.id).paginate(page=page, per_page=10)
    records = pagination.items
    return render_template('store/index.html', title='Store Inventory', records=records, pagination=pagination)


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
            item_name=row['name'],
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