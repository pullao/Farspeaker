import flask
from . import events, campaign

main = flask.Blueprint('main', __name__)

from . import routes
