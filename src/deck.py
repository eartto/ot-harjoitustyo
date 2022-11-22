import random


class Deck:
    def __init__(self):

        self.deck = []

        suits = ["diamonds","clubs","hearts","spades"]

        # 11=jack, 12=queen, 13=king, 14=ace
        values = range(2,15)

        for s in suits:
            for v in values:
                self.deck.append(f'{v} of {s}')

    def printDeck(self):

        print(self.deck)

    def deckLength(self):

        return len(self.deck)
        
