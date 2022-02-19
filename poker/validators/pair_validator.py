from poker.validators import AbstractValidator
from typing import List

from poker.card import Card
from poker.validators import RankCountValidator


class PairValidator(AbstractValidator, RankCountValidator):
    def __init__(self, cards: List[Card]) -> None:
        self._cards = cards
        self._name = "Pair"

    def is_valid(self) -> bool:
        ranks_with_pair = self._ranks_with_target_count(2)
        return len(ranks_with_pair) == 1

    def valid_cards(self) -> List[Card]:
        ranks_with_pair = self._ranks_with_target_count(2)
        _valid_cards = [
            card
            for card in self._cards
            if card.rank in ranks_with_pair.keys()
        ]

        return _valid_cards
