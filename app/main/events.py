import flask
import flask_socketio
from .. import socketio
import random
from . import tokenizer
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
        messageString = rollString + " -->"
        resultsList = list()
        total = 0
        for x in parsedList:
            result = x.calcValue()
            total = x.modifyTotal(total, result)
            resultsList = resultsList + [result]
            messageString = messageString + " " + x.sign + " " + result
        messageString = messageString + " = " + total
        print messageString

    else:
        room = flask.session.get('room')
        flask_socketio.emit('message', {'msg': flask.session.get('name') + ':' + message['msg']}, room=room)


def parseRoll(newRoll):
    unparsedList = tokenizer.rollTokenize(list(), newRoll)
    parsedList = list()
    for x in unparsedList:
        diceroll = roll.DiceRoll(x)
        parsedList = parsedList + [diceroll]
    return parsedList