from typing import List
from poker.card import Card

class TwoPairValidator:
    def __init__(self, cards:List[Card]) -> None:
        self._cards = cards
        self._name = "Two Pair"

    def is_valid(self) -> bool:
        ranks_with_pair = self._ranks_with_target_count(2)
        return len(ranks_with_pair) >= 2


    def valid_cards(self) -> List[Card]:
        ranks_with_pair = self._ranks_with_target_count(2)
        _valid_cards = [
                card 
                for card in self._cards 
                if card.rank in ranks_with_pair.keys()
                ]


        return _valid_cards



    def _ranks_with_target_count(self, target_count: int) -> dict:
        '''
        coupled with _card_rank_counts() method
        '''
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == target_count
        }

    @property
    def _card_rank_counts(self) -> dict:
        '''
        coupled with _ranks_with_target_count() method
        '''

        card_rank_count = {}
        for card in self._cards:
            # if the key already exists, do nothing
            card_rank_count.setdefault(card.rank, 0)
            card_rank_count[card.rank] += 1

        return card_rank_count