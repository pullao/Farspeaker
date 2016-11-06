import json
from . import message

class Campaign(object):

	dataPath='app/Data/'
	saveFile=None
	data = { 'name': 'New Campaign', 'participants': [], 'messages': {}}


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

			for i in range(0,len(self.data['messages']['main'])):
				self.data['messages']['main'][i]=message.Message.fromString(self.data['messages']['main'][i])
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
		for i in range(0,len(self.data['messages']['main'])):
			self.data['messages']['main'][i]=str(self.data['messages']['main'][i])
		with open(self.saveFile, 'w') as f:
			json.dump(self.data, f)
		#This is not a good way to handle this, replace this code
		for i in range(0,len(self.data['messages']['main'])):
			self.data['messages']['main'][i]=message.Message.fromString(self.data['messages']['main'][i])


	def getID (self, thread):
		if not thread in self.data['messages']:
			return -1
		if len(self.data['messages'][thread])==0:
			return 0
		return self.data['messages'][thread][-1].ID+1
