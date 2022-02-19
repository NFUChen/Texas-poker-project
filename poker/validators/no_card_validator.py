from poker.validators import AbstractValidator
from typing import List
from poker.card import Card


class NoCardsValidator(AbstractValidator):
    def __init__(self, cards: List[Card]) -> None:
        self._cards = cards
        self._name = "No Card"

    def is_valid(self) -> bool:
        return len(self._cards) == 0

    def valid_cards(self) -> List[Card]:
        return []
