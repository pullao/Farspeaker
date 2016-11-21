import flask
import flask_socketio
from .. import socketio
import random
from . import tokenizer
from . import activeCampaign
from . import message
import roll



@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    # Removing this feature the easy way
    room = flask.session.get('room')
    flask_socketio.join_room(room)
    # flask_socketio.emit('status', {'msg': flask.session.get('name') + ' has joined.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    parseMessage(message)

@socketio.on('character', namespace='/chat')
def character(message):
    """Sent by a client when the user entered a new character.
    Used to switch to a different alias"""
    if message['msg']=='resetchar':
        flask.session['character']=None
    else:
        flask.session['character']=message['msg']

@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = flask.session.get('room')
    flask_socketio.leave_room(room)
    flask_socketio.emit('status', {'msg': flask.session.get('name') + ' has left the room.'}, room=room)

def parseMessage(msg):
    print (msg)
    content=msg['msg']
    print (content)
    if content.startswith('/roll'):
        #room = flask.session.get('room')
        #flask_socketio.emit('status', {'msg': flask.session.get('name') + ' rolled a ' + str(random.randint(1,6))})
        rollString = content[5:]
        parsedList = parseRoll(rollString)
        msgString = flask.session.get('name') + " rolled:" + rollString + " -->"
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
        msgString = msgString + diceIntermediates + " = " + str(total)
        room = flask.session.get('room')
        flask_socketio.emit('diceroll', {'msg': msgString}, room=room)

    else:
        thread = msg['thread']
        try:
            character = flask.session.get('character')
        except:
            character = None
        transmission=message.Message(activeCampaign.getID(thread),
            flask.session.get('name'),msg['msg'],character=character)
        print(transmission);
        activeCampaign.data['messages'][thread].append(transmission);
        activeCampaign.save()
        flask_socketio.emit('message', {'msg': transmission.sender+': '+transmission.text, 'thread': thread}, room=flask.session.get('room'))


def parseRoll(newRoll):
    plusString = "+ " + newRoll
    unparsedList = tokenizer.rollTokenize(list(), plusString)
    parsedList = list()
    for x in unparsedList:
        diceroll = roll.DiceRoll(x)
        parsedList = parsedList + [diceroll]
    return parsedList