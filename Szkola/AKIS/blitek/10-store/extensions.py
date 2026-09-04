from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'auth.login' # type: ignore
login_manager.login_message = 'Strona dostępna dla zalogowanych użytkowników'
login_manager.login_message_category = 'warning'