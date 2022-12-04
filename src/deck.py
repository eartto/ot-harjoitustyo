import random
from card import Card


class Deck:
    def __init__(self):

        self.deck = []
        self.card = Card

        suits = ["diamonds", "clubs", "hearts", "spades"]

        # 11=jack, 12=queen, 13=king, 14=ace
        values = range(2, 15)

        for suit in suits:
            for value in values:
                self.deck.append(self.card(suit, value))

        random.shuffle(self.deck)        

    def print_deck(self):

        print(self.deck)

    def deal_cards(self, hand):
        
        rando_card = random.choice(self.deck)
        self.deck.remove(rando_card)
        hand.append(rando_card)
        
        return rando_card
    
    def __len__(self):
        return len(self.deck)

 

