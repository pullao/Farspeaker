import pytest
import roll
import tokenizer
import exceptions

def test_simpleRolls():
	for x in range(0, 100):
		diceroll = roll.DiceRoll("+ 1d6")
		result = diceroll.calcValue()
		assert result < 7
		assert result > 0

def test_modifyTotal():
	total = 0
	diceroll = roll.Diceroll("+ 1d6")
	result = diceroll.calcValue()
	total = diceroll.modifyTotal(total, result)
	assert total < 7
	assert total > 0
	total2 = 0
	diceroll2 = roll.Diceroll("- 1d6")
	result2 = diceroll2.calcValue()
	total2 = diceroll2.modifyTotal(total2, result2)
	assert total2 < 7
	assert total2 > 0

def test_rollZero():
	diceroll = roll.Diceroll("+ 0d6")
	result = diceroll.calcValue()
	assert result == 0
	diceroll = roll.Diceroll("+ 6d0")
	result = diceroll.calcValue()
	assert result == 0

def test_Tokenize():
	rollstring = "+ 1d6 + 2d6 + 3d6 - 4d6"
	tokened = tokenizer.rollTokenize(list(), rollstring)
	assert tokened == ["+ 1d6 ","+ 2d6 ","+ 3d6 ","- 4d6"]

def test_incorrectSign():
	with pytest.raises(DiceRollException):
		roll.Diceroll("1d6")
	

        