

class Card:
    """Class, that works as a card object.

    Attributes:
        value: Cards normal value.
        suit: Cards suit.
        jackvalue: Cards value in blackjack.
    """
    def __init__(self, suit, value, jackvalue):
        self.value = value
        self.suit = suit
        self.jackvalue = jackvalue

    def getJackvalue(self):
        return self.jackvalue

    def setJackvalue(self, newvalue):
        self.jackvalue = newvalue


    def __repr__(self):
        value = self.value
        suit = self.suit
        card = f"{value} of {suit}"

        return card

    def __str__(self):
        value = self.value
        suit = self.suit
        card = f"{value}_of_{suit}"

        return card