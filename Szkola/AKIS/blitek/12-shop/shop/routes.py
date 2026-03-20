from . import store_bp
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from extentions import db

@store_bp.route('/store')
@login_required
def index():
    products = Product.query.all()
    return render_template('store/index.html', products=products)
