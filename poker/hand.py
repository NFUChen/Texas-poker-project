from typing import Callable, List, Tuple

from poker.card import Card
from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardsValidator,
)


class Hand:
    '''
    Similar to stragy pattern, the validator classes can be swaped with other algorithms in any order.
    '''
    ALL_VALIDATOR_CLASSES: Tuple = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardsValidator,
    )

    def __init__(self) -> None:
        self.cards = []

    def __repr__(self) -> str:
        cards_as_string = ", ".join([str(card) for card in self.cards])

        return cards_as_string

    def add_cards(self, cards: List[Card]) -> None:
        cards_copy = self.cards[:]
        cards_copy.extend(cards)
        cards_copy.sort()

        self.cards = cards_copy

    def best_rank(self) -> str:
        for validator_class in self.ALL_VALIDATOR_CLASSES:
            current_rank_validator = validator_class(cards=self.cards)
            if current_rank_validator.is_valid():
                return current_rank_validator._name
