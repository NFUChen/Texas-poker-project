from typing import List
from poker.card import Card


class StraightFlushValidator:
    def __init__(self, cards: List[Card]) -> None:
        self._cards = cards
        self._name = "Straight Flush"

    def is_valid(self) -> bool:
        if self._iterate_five_cards_to_check_have_unique_suit():
            return True

        return False

    def valid_cards(self) -> List[Card]:
        # get the final batch of valid straight flush
        _valid_cards = self._straight_flush_card_batches[-1]
        return _valid_cards

    #_______________________________Helper Function____________________________#

    @property
    def _straight_flush_card_batches(self) -> List[List[Card]]:
        return [
            five_cards_batch
            for five_cards_batch in self._get_collections_of_valid_straight_cards()
            if (len({card.suit for card in five_cards_batch}) == 1)

        ]

    def _iterate_five_cards_to_check_have_unique_suit(self) -> bool:
        for current_five_cards in self._get_collections_of_valid_straight_cards():
            unique_suits_in_current_five_cards = {
                card.suit
                for card in current_five_cards
            }  # set comprehension
        # if only one suit presenting, it is definitly a straight flush
        return len(unique_suits_in_current_five_cards) == 1

    def _get_collections_of_valid_straight_cards(self) -> List[List[Card]]:
        curr_idx = 0
        final_idx = len(self._cards) - 1
        collections_of_valid_straight_cards = []
        while (curr_idx + 4 <= final_idx):
            current_five_cards = self._cards[curr_idx: curr_idx+5]
            current_five_cards_idx = [card.rank_index
                                      for card in current_five_cards]

            if self._every_element_increasing_by_1(current_five_cards_idx):
                collections_of_valid_straight_cards.append(current_five_cards)

            curr_idx += 1

        return collections_of_valid_straight_cards

    def _every_element_increasing_by_1(self, rank_indexes: List[int]) -> bool:

        return rank_indexes == list(range(rank_indexes[0],
                                          rank_indexes[-1] + 1))
