
from typing import List
from poker.card import Card
from poker.validators import FiveCardRanksInARowValidator


class StraightValidator(FiveCardRanksInARowValidator):
    def __init__(self, cards: List[Card]) -> None:
        self._cards = cards
        self._name = "Straight"

    def is_valid(self) -> bool:
        # becomes optional, since self.__every_element_increasing_by_1 will do the check for us
        # if len(self._cards) < 5:
        #     return False

        collections_of_valid_straight_cards = self._get_collections_of_valid_straight_cards()

        return len(collections_of_valid_straight_cards) >= 1

    def valid_cards(self) -> List[Card]:
        collections_of_valid_straight_cards: List[List[Card]
                                                  ] = self._get_collections_of_valid_straight_cards()
        # the last one is the best one, since the card is sorted
        _valid_card: List[Card] = collections_of_valid_straight_cards[-1]
        return _valid_card
