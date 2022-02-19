from typing import Callable, List, Tuple

from poker.card import Card
from poker.validators import (
    NoCardsValidator,
    HighCardValidator,
    PairValidator,
    TwoPairValidator,
    ThreeOfAKindValidator,
    StraightValidator,
    FlushValidator,
    FullHouseValidator,
    FourOfAKindValidator,

)


class Hand:
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

    @property
    def amount_of_cards_hold(self) -> int:
        return len(self.cards)

    @property
    def _rank_validations_from_best_to_worst(self) -> Tuple[Tuple[str, Callable]]:
        '''
        Helper property of .best_rank() method, 
        which the returned tuple (which will be unpacked as well) will be iterated over, 
        '''
        return (
            ("Royal FLush", self._royal_flush),
            ("Straight Flush", self._straight_flush),
            ("Four of A Kind", FourOfAKindValidator(cards=self.cards).is_valid),
            ("Full House", FullHouseValidator(cards=self.cards).is_valid),
            ("Flush", FlushValidator(cards=self.cards).is_valid),
            ("Straight", StraightValidator(cards=self.cards).is_valid),
            ("Three of A Kind", ThreeOfAKindValidator(cards=self.cards).is_valid),
            ("Two Pair", TwoPairValidator(cards=self.cards).is_valid),
            ("Pair", PairValidator(cards=self.cards).is_valid),
            ("High Card", HighCardValidator(cards=self.cards).is_valid),
            ("No Cards", NoCardsValidator(cards=self.cards).is_valid)
        )

    def best_rank(self) -> str:
        '''
        Figures out what is the best rank 
        using _rank_validations_from_best_to_worst helper property
        '''

        for rank_name_with_validator_tuple in self._rank_validations_from_best_to_worst:
            rank_name, validator_func = rank_name_with_validator_tuple
            if validator_func():
                return rank_name

    def _royal_flush(self) -> bool:
        is_straight_flush = self._straight_flush()
        if not is_straight_flush:
            # if the .amount_of_cards_hold is < 5, returning False
            return False

        is_royal = (self.cards[-1].rank == "Ace" and
                    self.cards[0].rank == "10")

        return is_straight_flush and is_royal

    def _straight_flush(self) -> bool:
        return (
            FlushValidator(cards=self.cards) and
            StraightValidator(cards=self.cards).is_valid()
        )
