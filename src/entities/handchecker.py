

class HandChecker:
    """Class, that works as a tool to confirm handvalues.

    Attributes:
        none
    """

    def __init__(self):
        pass



    def bust_hand(self, handtotal):
        """Returns true if hand is a bust.

        Args:
            handtotal: int, hands total value that you want checked.
        """

        if handtotal > 21:
            return True
        else:
            return False


    def hand_total(self, hand):
        """Loops through hand and returns its hand total.

        Args:
            hand: list, a hand whose total you want confirmed.
        """
        total = 0
        if len(hand) == 2 & (hand[0].getJackvalue() + hand[1].getJackvalue() == 21):
            return 21
        else:
            for card in hand:

                total += card.getJackvalue()

            return total


    def switch_aces(self, hand):
        """Loops through hand while hand total is more than 21 and
         switches any aces from eleven to one.

        Args:
            hand: list, a hand whose aces you wish to switch.
        """

        for card in hand:
            if (self.hand_total(hand) > 21) & (card.getJackvalue() == 11):
                card.setJackvalue(1)
