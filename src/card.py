

class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

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