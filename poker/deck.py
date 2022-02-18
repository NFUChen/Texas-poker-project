from typing import List
from poker.card import Card
import random  # for shuffling cards


class Deck:
    def __init__(self) -> None:
        self._cards: List = []

    def __len__(self):
        return len(self._cards)

    def add_cards(self, cards: List[Card]) -> None:
        self._cards.extend(cards)

    def remove_cards(self, number: int) -> List[Card]:

        cards_to_removed: List[Card] = self._cards[:number]
        # not del cards_to_removed, it will delete the variabel "cards_to_removed with garbage collector"
        del self._cards[:number]

        return cards_to_removed

    def shuffle(self) -> None:
        random.shuffle(self._cards)  # in-place operating, returing None
