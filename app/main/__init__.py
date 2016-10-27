import flask
from . import campaign

main = flask.Blueprint('main', __name__)
activeCampaign = campaign.Campaign()

from . import events, routes
