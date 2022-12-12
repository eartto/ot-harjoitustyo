import unittest


from entities.handchecker import HandChecker
from entities.card import Card


class TestCard(unittest.TestCase):

    def setUp(self):
        self.handchecker = HandChecker()
        self.hand = []

    def test_hand_total(self):
        card1 = Card("diamonds",7,7)
        card2 = Card("diamonds",8,8)
        card3 = Card("hearts",13,10)

        self.hand.append(card1)
        self.hand.append(card2)
        self.hand.append(card3)

        self.assertEqual(self.handchecker.hand_total(self.hand), 25)


    def test_bust_hand(self):
        card1 = Card("diamonds",7,7)
        card2 = Card("diamonds",8,8)
        card3 = Card("hearts",13,10)

        self.hand.append(card1)
        self.hand.append(card2)
        self.hand.append(card3)

        total = self.handchecker.hand_total(self.hand)


        self.assertEqual(self.handchecker.bust_hand(total), True)