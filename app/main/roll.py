import random
import farspeakerexceptions

class DiceRollError(Exception):
    pass

class DiceRoll:
   'base class for a single roll'

   def __init__(self, rollString):
      self.rawString = rollString
      self.sign = self.rawString[0]
      if(self.sign != "+" and self.sign != "-" and self.sign != "*" and self.sign != "/"):
         raise DiceRollError(rollString)
   
   def calcValue(self):
      rollString = self.rawString[1:]
      rollString = rollString.replace(" ", "")
      if(rollString.isdigit()):
         return int(rollString)
      self.dicenum = rollString[0]
      rollString = rollString[1:]
      rollString = rollString[1:]
      self.resultList = self.rollDice(self.dicenum, rollString)
      total = 0
      for x in self.resultList:
         total += int(x)
      return total

   def rollDice(self, num, sides):
      resultList = list()
      for x in range(0, int(num)):
         result = random.randint(1, int(sides))
         resultList = resultList + [result]
      return resultList

   def modifyTotal(self, total, result):
      if(self.sign == '+'):
         return total + result
      elif(self.sign == "-"):
         return total - result
      elif(self.sign == "*"):
         return total * result
      elif(self.sign == "/"):
         return total / result