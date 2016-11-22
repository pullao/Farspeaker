import character

class User:
   'base class for a user'

   def __init__(self, playername):
   	self.name = playername
   	self.characters= []

   	def addCharacter(self, url):
   		newchar = character.Character(url)
   		self.characters.append(newchar)