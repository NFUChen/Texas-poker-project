
class Player:
    def __init__(self, name, hand_obj) -> None:
        self.name = name 
        self.hand = hand_obj

    
    def best_hand(self):
        return self.hand.best_rank()
