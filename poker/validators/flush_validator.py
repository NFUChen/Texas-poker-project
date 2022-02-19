from poker.validators import AbstractValidator
from typing import List

from poker.card import Card
from poker.validators import RankCountValidator  # for rank count


class FlushValidator(AbstractValidator, RankCountValidator):
    def __init__(self, cards: List[Card]) -> None:
        self._cards = cards
        self._name = "Flush"

    def is_valid(self) -> bool:
        # {"Heart" : 6}
        suits_that_occur_5_or_more_times = self._get_suits_that_occur_5_or_more_times()

        return len(suits_that_occur_5_or_more_times) == 1

    def valid_cards(self) -> List[Card]:
        suits_that_occur_5_or_more_times: dict = self._get_suits_that_occur_5_or_more_times()

        _valid_cards = [card
                        for card in self._cards
                        if card.suit in suits_that_occur_5_or_more_times.keys()]

        return _valid_cards[-5:]

#________________________ Helper Function _____________________________________#

    def _get_suits_that_occur_5_or_more_times(self) -> dict:
        return {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5}  # {"Heart" : 6}

    def _suits_with_target_count(self, target_count: int) -> dict:
        '''
        coupled with _card_suit_counts() method
        '''
        return {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count == target_count  # >=
        }

    @property
    def _card_suit_counts(self) -> dict:
        card_suit_count = {}
        for card in self._cards:
            # if the key already exists, do nothing
            card_suit_count.setdefault(card.suit, 0)
            card_suit_count[card.suit] += 1

        return card_suit_count
