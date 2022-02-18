from typing import List
from poker.card import Card
from poker.hand import Hand


class Player:
    def __init__(self, name: str, hand_obj: Hand) -> None:
        self.name = name
        self.hand = hand_obj

    def best_hand(self) -> str:
        return self.hand.best_rank()

    def add_cards(self, cards: List[Card]) -> None:
        self.hand.add_cards(cards)
