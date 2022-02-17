from typing import List
from poker.card import Card

class Deck:
    def __init__(self) -> None:
        self._cards:List = []
    
    def add_cards(self, cards:List[Card]) -> None:
        self._cards.extend(cards)

