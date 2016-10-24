import json

class Campaign(object):

	dataPath='../Data/'
	saveFile=None
	data = { 'name': 'New Campaign', 'participants': [], 'messages': {}}


	def __init__ (self, loadFrom=None):
		if loadFrom != None:
			self.load(loadFrom)

	def load (self, filename):
		with open(self.dataPath + filename, 'r') as f:
			self.data = json.load(f)

	def save (self,filename=None):
		if filename != None:
			self.saveFile=self.dataPath + filename
		with open(self.saveFile, 'w') as f:
			json.dump(self.data, f)