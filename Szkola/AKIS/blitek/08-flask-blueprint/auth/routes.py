from flask import Blueprint

auth_bp = Blueprint('auth', import_name=__name__)

@auth_bp.route(rule='/')
def index():
    return "Auth Dashboard"