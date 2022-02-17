
from typing import List
from poker.card import Card


class Hand:
    def __init__(self, cards:List[Card]) -> None:
        self.cards = cards

    def best_rank(self) -> str:
        


        
        

        ranks_with_three_of_a_kind = self._ranks_with_target_count(3)
        if len(ranks_with_three_of_a_kind) == 1:
            return "Three of A Kind"
        
        ranks_with_pairs = self._ranks_with_target_count(2)

        if len(ranks_with_pairs) == 1:
            return "Pair"
        if len(ranks_with_pairs) == 2:
            return "Two Pair"
            






        return "High Card"
    
    def _ranks_with_target_count(self, target_count:int) -> dict:
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
        for card in self.cards:
            card_rank_count.setdefault(card.rank, 0) # if the key already exists, do nothing
            card_rank_count[card.rank] += 1

        return card_rank_count

    
    @property
    def _card_suit_counts(self) -> dict:
        card_suit_count = {}
        for card in self.cards:
            card_suit_count.setdefault(card.suit, 0) # if the key already exists, do nothing
            card_suit_count[card.suit] += 1

        return card_suit_count


