import random

from .card import Card


class Deck:
    """Class, that creates and shuffles a deck, filled with card objects.

    Attributes:
        deck: List filled with cards.
        card: Card objects contained within deck.
    """
    def __init__(self):

        self.deck = []
        self.card = Card

        suits = ["diamonds", "clubs", "hearts", "spades"]

        # 11=jack, 12=queen, 13=king, 14=ace
        # Jackvalue is the cards value in blackjack
        values = range(2, 15)

        for suit in suits:
            for value in values:
                jackvalue = value
                if jackvalue == 14:
                    jackvalue = 11
                elif jackvalue > 10:
                    jackvalue = 10
                self.deck.append(self.card(suit, value, jackvalue))

        random.shuffle(self.deck)


    def deal_cards(self, hand):
        """Deals the top card to designated hand.

        Args:
            hand: a hand that you wish to deal a card to.
        """

        card = self.deck[0]
        self.deck.remove(card)
        hand.append(card)

        return card

    def __len__(self):
        return len(self.deck)
