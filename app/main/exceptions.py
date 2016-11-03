class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class DiceRollError(Error):
    """Exception raised for errors in the dice rool input."""