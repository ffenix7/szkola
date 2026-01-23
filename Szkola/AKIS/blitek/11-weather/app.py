from flask import Flask, Blueprint, render_template, request
import utils

main = Blueprint('main', __name__, template_folder='main/templates')


@main.route('/', methods=['GET', 'POST'])
def index():
	cities = utils.get_cities()
	selected = None
	weather = None
	air = None
	if request.method == 'POST':
		selected = request.form.get('city')
		if selected:
			weather = utils.get_weather(selected)
			air = utils.get_air_quality(selected)
	return render_template('main.html', cities=cities, selected=selected, weather=weather, air=air)


def create_app():
	app = Flask(__name__)
	app.register_blueprint(main)
	return app


if __name__ == '__main__':
	app = create_app()
	app.run(debug=True)

