from typing import List
from typing import List
from poker.card import Card

class Deck:
    def __init__(self) -> None:
        self.cards:List = []
    
    def add_cards(self, cards:List[Card]):
        self.cards.extend(cards)

