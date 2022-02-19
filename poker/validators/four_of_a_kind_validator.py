from poker.validators import AbstractValidator
from typing import List

from poker.card import Card
from poker.validators import RankCountValidator


class FourOfAKindValidator(AbstractValidator, RankCountValidator):
    def __init__(self, cards: List[Card]) -> None:
        self._cards = cards
        self._name = "Four of A Kind"

    def is_valid(self) -> bool:
        ranks_with_four_of_a_kind = self._ranks_with_target_count(4)

        return len(ranks_with_four_of_a_kind) == 1

    def valid_cards(self) -> List[Card]:
        ranks_with_four_of_a_kind = self._ranks_with_target_count(4)

        _valid_cards = [
            card
            for card in self._cards
            if card.rank in ranks_with_four_of_a_kind.keys()
        ]
        _valid_cards.sort()

        return _valid_cards
