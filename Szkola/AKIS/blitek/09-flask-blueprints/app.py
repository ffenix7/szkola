from flask import Flask
from flask_bs4 import Bootstrap
from main.routes import main_bp
import secrets
from auth.routes import auth_bp
from extentions import db, bcrypt, login_manager
from models import Users
import os

def create_app():
    #app config
    app = Flask(__name__)
    Bootstrap(app)

    app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

    #db config
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    os.makedirs(DATA_DIR, exist_ok=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(DATA_DIR, 'users.db')

    #extensions init
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    #blueprint config
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    #user loader
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))
    return app


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        db.create_all()
    app.run(debug=True)