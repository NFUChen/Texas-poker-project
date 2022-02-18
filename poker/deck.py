from typing import List

from poker.card import Card
import random  # for shuffling cards


class Deck:
    def __init__(self) -> None:
        self._cards: List = []

    def add_cards(self, cards: List[Card]) -> None:
        self._cards.extend(cards)

    def shuffle(self):
        random.shuffle(self._cards)  # in-place operating, returing None
