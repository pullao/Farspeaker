import flask
import flask_socketio
from .. import socketio
import random
from . import tokenizer
from . import activeCampaign
import roll


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = flask.session.get('room')
    flask_socketio.join_room(room)
    flask_socketio.emit('status', {'msg': flask.session.get('name') + ' has joined.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    parseMessage(message)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = flask.session.get('room')
    flask_socketio.leave_room(room)
    flask_socketio.emit('status', {'msg': flask.session.get('name') + ' has left the room.'}, room=room)

def parseMessage(message):
    print (message)
    content=message['msg']
    print (content)
    if content.startswith('/roll'):
        #room = flask.session.get('room')
        #flask_socketio.emit('status', {'msg': flask.session.get('name') + ' rolled a ' + str(random.randint(1,6))})
        rollString = content[5:]
        parsedList = parseRoll(rollString)
        messageString = flask.session.get('name') + " rolled:" + rollString + " -->"
        resultsList = list()
        total = 0
        diceIntermediates = ""
        for x in parsedList:
            result = x.calcValue()
            print result
            total = x.modifyTotal(total, result)
            resultsList = resultsList + [result]
            diceIntermediates = diceIntermediates + " " + x.sign + " " + str(result)
        diceIntermediates = diceIntermediates[2:]
        messageString = messageString + diceIntermediates + " = " + str(total)
        room = flask.session.get('room')
        flask_socketio.emit('diceroll', {'msg': messageString}, room=room)

    else:
        room = flask.session.get('room')
        transmission=flask.session.get('name') + ':' + message['msg']
        activeCampaign.data['messages'][room].append(transmission);
        print activeCampaign.data['messages'][room]
        activeCampaign.save()
        flask_socketio.emit('message', {'msg': transmission}, room=room)


def parseRoll(newRoll):
    plusString = "+ " + newRoll
    unparsedList = tokenizer.rollTokenize(list(), plusString)
    parsedList = list()
    for x in unparsedList:
        diceroll = roll.DiceRoll(x)
        parsedList = parsedList + [diceroll]
    return parsedList