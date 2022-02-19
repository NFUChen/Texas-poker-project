from typing import List
from poker.card import Card


class FiveCardRanksInARowValidator:
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
