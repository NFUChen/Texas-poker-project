from typing import List
from poker.card import Card


class HighCardValidator:
    def __init__(self, cards:List[Card]) -> None:
      self._cards = cards
      self._name = "High Card"

  
    def is_valid(self) -> bool:
      return len(self._cards) >= 2


    def valid_cards(self) -> List[Card]:
        return self._cards[-1:] # the card having the higest rank.
    

    


