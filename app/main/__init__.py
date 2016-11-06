import flask
from . import campaign

main = flask.Blueprint('main', __name__)
activeCampaign = campaign.Campaign("NewCampaign.txt")

from . import events, routes, message
