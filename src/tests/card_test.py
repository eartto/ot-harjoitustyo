import unittest


from entities.card import Card


class TestCard(unittest.TestCase):

    def setUp(self):
        pass

    def test_card_print(self):
        self.card = Card("diamonds", 11, 10)
        self.assertEqual(str(self.card), "11_of_diamonds")