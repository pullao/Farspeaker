import json
from . import message, user

class Campaign(object):

	dataPath='app/Data/'
	saveFile=None
	data = { 'name': 'New Campaign', 'participants': {}, 'messages': {}}


	def __init__ (self, loadFrom=None):
		#check and see if campaign is being loaded
		if loadFrom != None:
			self.load(loadFrom)
		else:
			self.createNew()

	def createNew(self):
		self.data['messages']['main']=[]

	def load (self, filename):
		#load and convert each message
		try:
			with open(self.dataPath + filename, 'r') as f:
				self.data = json.load(f)

			for thread in self.data['messages']:
				for i in range(0,len(self.data['messages'][thread])):
					self.data['messages'][thread][i]=message.Message.fromString(self.data['messages'][thread][i])
		#If there is an error, create a new file for loading
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
		## Iterate through each thread and convert each thread to a string for saving
		for thread in self.data['messages']:
			for i in range(0,len(self.data['messages'][thread])):
				self.data['messages'][thread][i]=str(self.data['messages'][thread][i])
		with open(self.saveFile, 'w') as f:
			json.dump(self.data, f, indent=4)
		#Convert it back to a dict
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

	"""method to add a user class to the participants dictionary in the data"""
	def addUser(player):
		if player in data['participants']:
			return 0
		else:
			data['participants'][player] = user.User(player)
			return 1