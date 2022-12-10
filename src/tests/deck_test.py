import unittest
from deck import Deck


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_deck_length(self):

        self.assertEqual(len(self.deck), 52)
