

class HandChecker:
    def __init__(self):
        pass


    
    def bust_hand(self, handtotal):

        if handtotal > 21:
            return True
        else:
            return False
        

    def hand_total(self, hand):

        total = 0
        if len(hand) == 2 & (hand[0].getJackvalue() + hand[1].getJackvalue() == 21):
            return 21
        else:
            for card in hand:
                
                total += card.getJackvalue()

            return total


    def switch_aces(self, hand):

        for card in hand:
            if (self.hand_total(hand) > 21) & (card.getJackvalue() == 11):
                card.setJackvalue(1)
