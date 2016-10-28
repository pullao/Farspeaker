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


if __name__ == '__main__':
	#rollist = rollTokenize(list(), "+ 4d6 + 3d8 - 2d2  ")
	#for x in rollist:
	#	print x
	#rollist2 = rollTokenize(list(), "/ 4d6 + askdmqwoebqwkpjeqw * 2d20141254")
	#for x in rollist2:
	#	print x
    rollist3 = rollTokenize(list(), "  1d6 + 2")
    for x in rollist3:
        print x