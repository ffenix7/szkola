from flask import Flask, render_template, request, redirect, url_for
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = random.randbytes(16)

users = []

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    user_form = UserForm()

    if user_form.validate_on_submit():
        users.append({
            'name': user_form.name.data,
            'email': user_form.email.data
        })
        return redirect(url_for('index'))

    return render_template(template_name_or_list='index.html', title='Home', users=users, user_form=user_form)

if __name__ == '__main__':
    app.run(debug=True)