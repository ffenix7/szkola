from flask_login import UserMixin
from extensions import db, login_manager


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(50), unique=True, nullable=False)
    user_password = db.Column(db.String(50), nullable=False)
    user_first_name = db.Column(db.String(20), nullable=False)
    user_last_name = db.Column(db.String(30), nullable=False)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    published_year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    cover_url = db.Column(db.String(255))


@login_manager.user_loader
def load_user(user_id: str):
    if user_id and str(user_id).isdigit():
        return User.query.get(int(user_id))
    return None
