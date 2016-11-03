import json

class Message(Object):

	def __init__(self,ID,user,text,character=None,thread='main'):
		self.text=text
		self.sender=user# TODO user.name
		self.id=ID
		#TODO
		#self.thread='main'
		#self.charName=character.name
		#self.picturePath=character.picturePath
		pass

	def __str__(self):
		ret={}
		ret['text']=self.text
		ret['sender']=self.sender
		ret['id']=self.ID
		#TODO
		#ret['thread']=self.thread
		#ret['charName']=self.charName
		#ret['picturePath']=self.picturePath
		return json.dumps(ret)

	def __lt__(self, other):
		if isinstance(other,Message):
			return self.ID<other.ID
		else:
			return self.ID<other

	def __gt__(self, other):
		if isinstance(other,Message):
			return self.ID>other.ID
		else:
			return self.ID>other

	def fromString(self, loadString):
		load=json.loads(loadString)
		self.text=load['text']
		self.sender=load['sender']
		self.ID=load['ID']
		##TODO
		#self.thread=load['thread']
		#self.charName=load['charName']
		#self.picturePath=load['picturePath']



