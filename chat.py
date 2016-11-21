#!/bin/env python
from app import createApp, socketio
import sys, getopt

app = createApp(debug=True)
	

if __name__ == '__main__':
	farport = 5000
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hp",["port="])
	except getopt.GetoptError:
		print 'chat.py -p <portnumber>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'chat.py -p <portnumber>'
			sys.exit()
		elif opt in ("-p", "--port"):
			farport = int(arg)
	print 'Running on port: ' + str(farport)
	socketio.run(app, host='0.0.0.0', port=farport)
