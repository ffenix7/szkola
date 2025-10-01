from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired
import secrets
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
Bootstrap(app)

def load_students():
    try:
        with open('students.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_students(students):
    with open('students.json', 'w', encoding='utf-8') as f:
        json.dump(students,f, indent=4)

class RegisterForm(FlaskForm):
    first_name = StringField('Imię', validators=[DataRequired()])
    last_name = StringField('Nazwisko', validators=[DataRequired()])
    class_name = StringField('Klasa', validators=[DataRequired()])
    submit = SubmitField('Dodaj ucznia')

@app.route('/')
def index():
    students = load_students()
    return render_template('index.html', title="Strona główna", students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = RegisterForm()
    if form.validate_on_submit():
        file = load_students()
        new_student = {
            "id": len(file),
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'class_name': form.class_name.data
        }
        file.append(new_student)
        save_students(file)
        
        flash(f'Uczeń {form.first_name.data} {form.last_name.data} z klasy {form.class_name.data} został dodany!', 'success')
        return redirect(url_for('index'))
    return render_template('add_student.html', title="Dodaj ucznia", form=form)

@app.route('/delete_student/<int:id>', methods=['POST'])
def delete_student(id):
    students = load_students()
    if 0 <= id < len(students):
        students.pop(id)
        save_students(students)
        flash('Uczeń został usunięty.', 'success')
    else:
        flash('Nieprawidłowy ID ucznia.', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
