from flask import Blueprint, render_template

main_bp = Blueprint('main', import_name=__name__, template_folder='templates')


@main_bp.route('/')
@main_bp.route('/home', endpoint='home')
def index():
    return render_template('main/index.html', title='Home Page')