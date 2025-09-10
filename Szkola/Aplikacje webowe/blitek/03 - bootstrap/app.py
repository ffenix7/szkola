import flask 
from flask_bs4 import Bootstrap

app = flask.Flask(__name__)
bootstrap = Bootstrap(app=app)

users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
    {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
]

@app.route(rule='/')
def index():
    return flask.render_template(template_name_or_list='index.html', title='Home', users=users)

@app.route(rule='/user/<int:id>')
def user(id):
    for user in users:
        if user['id'] == id:
            user = next((user for user in users if user['id'] == id), None)
            return flask.render_template(template_name_or_list='user.html', user=user, title="Profil użytkownika")

if __name__ == '__main__':
    app.run(debug=True)