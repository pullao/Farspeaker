import random

class DiceRollError(Exception):
    pass

class DiceRoll:
   'base class for a single roll.'

   def __init__(self, rollString):
      self.rawString = rollString
      self.sign = self.rawString[0]
      if(self.sign != "+" and self.sign != "-" and self.sign != "*" and self.sign != "/"):
         raise DiceRollError(rollString)

   """From the string, calculates the value of the dice rolls, returns an int with the total"""
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

   """Rolls a set of dice and returns the results as a list of the individual dice
      For example, 2d6 would be returned as [2, 4], not 6"""
   def rollDice(self, num, sides):
      resultList = list()
      for x in range(0, int(num)):
         result = random.randint(1, int(sides))
         resultList = resultList + [result]
      return resultList

   """Modifies a number by the result of the diceroll. uses the dicerolls stored self.sign to figure out what method to use"""
   def modifyTotal(self, total, result):
      if(self.sign == '+'):
         return total + result
      elif(self.sign == "-"):
         return total - result
      elif(self.sign == "*"):
         return total * result
      elif(self.sign == "/"):
         return total / result