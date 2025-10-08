from flask import Blueprint

blog_bp = Blueprint('blog', import_name=__name__)

@blog_bp.route(rule='/')
def index():
    return "Blog Dashboard"