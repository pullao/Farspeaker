import flask
import flask_socketio

socketio = flask_socketio.SocketIO()

from .main import main as main_blueprint

def createApp(debug=False):
    """Create an application."""
    app = flask.Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app


