import roll

"""A function for tokenizing a string into a set of roll strings
   For example + 3d4 - 2d6 + 1d8 becomes ["+ 3d4", "- 2d6", "+ 1d8"]
   A recursive function"""
def rollTokenize(rollList, messageString):
    if((len(messageString) == 0) or (messageString.isspace())):
        return rollList
    else:
        for x in range(1, len(messageString)):
            if((messageString[x] == '+') or (messageString[x] == '-') or (messageString[x] == '*') or (messageString[x] == '/')):
            	roll = messageString[:x]
            	rollList = rollList + [roll]
            	return rollTokenize(rollList, messageString[x:])
        roll = messageString
        rollList = rollList + [roll]
        return rollTokenize(rollList, "")

"""Function to parse a roll string. Takes the string and turns it into a list of dicerolls
    Functionally acts as a factory for Dicerolls, moving that code out of the message parsing"""
def parseRoll(newRoll):
    plusString = "+ " + newRoll
    unparsedList = rollTokenize(list(), plusString)
    parsedList = list()
    for x in unparsedList:
        diceroll = roll.DiceRoll(x)
        parsedList = parsedList + [diceroll]
    return parsedList