import flask
from . import routes, events

main = flask.Blueprint('main', __name__)
