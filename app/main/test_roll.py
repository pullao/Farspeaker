import pytest
import roll

def test_simpleRolls():
	for x in range(0, 100):
		diceroll = roll.DiceRoll("+ 1d6")
		result = diceroll.calcValue()
		assert result < 7
		assert result > 0