from poker.validators import AbstractValidator
from typing import List

from poker.card import Card
from poker.validators import (
    ThreeOfAKindValidator,
    PairValidator
)


class FullHouseValidator(AbstractValidator):
    def __init__(self, cards: List[Card]) -> None:
        self._cards = cards
        self._name = "Full House"

    def is_valid(self) -> bool:
        return (
            ThreeOfAKindValidator(cards=self._cards).is_valid() and
            PairValidator(cards=self._cards).is_valid()
        )

    def valid_cards(self) -> List[Card]:
        three_of_a_kind_cards = ThreeOfAKindValidator(
            cards=self._cards).valid_cards()
        pair_cards = PairValidator(cards=self._cards).valid_cards()
        _valid_cards = [*three_of_a_kind_cards,
                        *pair_cards]  # unpacking the element in the list

        _valid_cards.sort()

        return _valid_cards
