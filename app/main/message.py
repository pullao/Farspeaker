import json

class Message(object):

	@staticmethod
	def fromString(loadString):
		load=json.loads(loadString)
		text=load['text']
		sender=load['sender']
		ID=load['ID']
		##TODO @jake I dont think we need 'thread' depends on implementation i suppose
		#self.thread=load['thread']
		#self.charName=load['charName']
		#self.picturePath=load['picturePath']
		return Message(ID,sender,text)

	def __init__(self,ID,user,text,character=None,thread='main'):
		self.text=text
		self.sender=user# TODO user.name
		self.ID=ID
		#TODO I dont think we need 'thread' 
		#self.thread='main'
		#self.charName=character.name
		#self.picturePath=character.picturePath
		pass

	def __str__(self):
		ret={}
		ret['text']=self.text
		ret['sender']=self.sender
		ret['ID']=self.ID
		#TODO I dont think we need 'thread' 
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



