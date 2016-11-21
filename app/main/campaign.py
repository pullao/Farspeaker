import json
from . import message, user

class Campaign(object):

	dataPath='app/Data/'
	saveFile=None
	data = { 'name': 'New Campaign', 'participants': {}, 'messages': {}}


	def __init__ (self, loadFrom=None):
		if loadFrom != None:
			self.load(loadFrom)
		else:
			self.createNew()

	def createNew(self):
		self.data['messages']['main']=[]

	def load (self, filename):
		try:
			with open(self.dataPath + filename, 'r') as f:
				self.data = json.load(f)

			for thread in self.data['messages']:
				for i in range(0,len(self.data['messages'][thread])):
					self.data['messages'][thread][i]=message.Message.fromString(self.data['messages'][thread][i])
		except:
			print "Load File Not found"
			# TODO: for now just create new, eventually prompt the user
			self.createNew()


	def save (self,filename=None):
		print "Saving..."
		if filename != None:
			self.saveFile=self.dataPath + filename
		else: 
			self.saveFile=self.dataPath+self.data['name'].replace(' ','')+'.txt'
		##TODO add another loop to handle multiple threads
		for thread in self.data['messages']:
			for i in range(0,len(self.data['messages'][thread])):
				self.data['messages'][thread][i]=str(self.data['messages'][thread][i])
		with open(self.saveFile, 'w') as f:
			json.dump(self.data, f, indent=4)
		#This is not a good way to handle this, replace this code
		for thread in self.data['messages']:
			for i in range(0,len(self.data['messages'][thread])):
				self.data['messages'][thread][i]=message.Message.fromString(self.data['messages'][thread][i])


	def getID (self, thread):
		if not thread in self.data['messages']:
			return -1
		if len(self.data['messages'][thread])==0:
			return 0
		return self.data['messages'][thread][-1].ID+1

	def addUser(player):
		if player in data['participants']:
			return 0
		else:
			data['participants'][player] = user.User(player)
			return 1