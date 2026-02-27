import os
import secrets
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from extensions import bootstrap, db, login_manager
from forms import BookForm, LoginForm, RegistrationForm
from models import Book, User

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
DATABASE_PATH = os.path.join(DATA_DIR, "books.db")

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
login_manager.init_app(app)
bootstrap.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET"])
def index():
    books = Book.query.order_by(Book.title).all()
    return render_template("index.html", books=books)

@app.route("/add", methods=["GET", "POST"])
@login_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data.strip(),
            author=form.author.data.strip(),
            genre=form.genre.data.strip(),
            published_year=form.published_year.data,
            description=form.description.data.strip(),
            cover_url=(form.cover_url.data or "").strip() or None,
        )
        db.session.add(book)
        db.session.commit()
        flash("Książka została dodana.", "success")
        return redirect(url_for("index"))

    return render_template("add_edit_book.html", form=form, heading="Dodaj książkę")

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
@login_required
def edit_book(book_id: int):
    book = Book.query.get_or_404(book_id)
    form = BookForm(obj=book)

    if form.validate_on_submit():
        book.title = form.title.data.strip()
        book.author = form.author.data.strip()
        book.genre = form.genre.data.strip()
        book.published_year = form.published_year.data
        book.description = form.description.data.strip()
        book.cover_url = (form.cover_url.data or "").strip() or None
        db.session.commit()
        flash("Dane książki zostały zaktualizowane.", "success")
        return redirect(url_for("index"))

    return render_template("add_edit_book.html", form=form, heading="Edytuj książkę")

@app.post("/delete/<int:book_id>")
@login_required
def delete_book(book_id: int):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash("Książka została usunięta.", "info")
    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("Jesteś już zalogowany.", "info")
        return redirect(url_for("index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        normalized_email = form.user_email.data.strip().lower()
        if User.query.filter_by(user_email=normalized_email).first():
            flash("Podany adres e-mail jest już zajęty.", "danger")
        else:
            user = User(
                user_email=normalized_email,
                user_first_name=form.user_first_name.data.strip(),
                user_last_name=form.user_last_name.data.strip(),
                user_password=form.password.data,
            )
            db.session.add(user)
            db.session.commit()
            flash("Konto zostało utworzone. Możesz się zalogować.", "success")
            return redirect(url_for("login"))

    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("Jesteś już zalogowany.", "info")
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.user_email.data.strip().lower()).first()
        if user and user.user_password == form.password.data:
            login_user(user)
            flash("Zalogowano pomyślnie.", "success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("index"))
        flash("Niepoprawny e-mail lub hasło.", "danger")

    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Zostałeś wylogowany.", "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=5000)
