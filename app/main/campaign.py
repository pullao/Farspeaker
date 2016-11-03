import json

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

			for i in range(0,len(data['messages']['main'])):
				data['messages']['main'][i]=Message.fromString(data['messages']['main'][i])
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
		for i in range(0,len(data['messages']['main'])):
			data['messages']['main'][i]=str(data['messages']['main'][i])
		with open(self.saveFile, 'w') as f:
			json.dump(self.data, f)