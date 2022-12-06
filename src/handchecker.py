

class HandChecker:
    def __init__(self):
        
        self.pwins = False
        self.hwins = False
        self.push = False

    def check_hands(self, p_hand, d_hand):
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
                if (card.getJackvalue() == 11) & (total + card.getJackvalue() > 21):
                    j = card.setJackvalue(1)
                    total += j
                else:
                    total += card.getJackvalue()


            return total

    def n_aces(self, hand):
        total = 0
        for card in hand:
            if card.getJackvalue == 11:
                total += 1
        return total

    def switch_aces(self, hand):

        pass