from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from extentions import db
from models import Inventory
from . import store_bp

@store_bp.route('/')
@login_required
def index():
    return render_template('store/index.html', title='Store Inventory')