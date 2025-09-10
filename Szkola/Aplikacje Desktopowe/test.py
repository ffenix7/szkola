import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/user/<name>')
def user(name):
    return f"<h1>Witaj {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)