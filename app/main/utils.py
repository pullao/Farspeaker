from flask import session
from .. import socketio

def ParseMessage(message):
	print (message)
	room = session.get('room')
	emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)