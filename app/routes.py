from app import flask_app
import flask


@flask_app.route('/')
def index():
    return flask.render_template('index.html')

