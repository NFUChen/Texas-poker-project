from typing import List
from poker.card import Card
from poker.validators import FiveCardRanksInARowValidator, StraightFlushValidator


class RoyalFlushValidator(FiveCardRanksInARowValidator):
    def __init__(self, cards: List[Card]) -> None:
        self._cards = cards
        self._name = "Royal Flush"

    def is_valid(self) -> bool:
        straight_flush_validator = StraightFlushValidator(cards=self._cards)

        if straight_flush_validator.is_valid():
            valid_straight_flush_cards = straight_flush_validator.valid_cards()
            is_royal = (valid_straight_flush_cards[-1].rank == "Ace" and
                        valid_straight_flush_cards[0].rank == "10")

            return is_royal
        return False

    def valid_cards(self) -> List[Card]:
        return StraightFlushValidator(cards=self._cards).valid_cards()

    #_______________________________Helper Function____________________________#
