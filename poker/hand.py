
from typing import List
from poker.card import Card


class Hand:
    def __init__(self, cards:List[Card]) -> None:
        self.cards = cards

    def best_rank(self) -> str:
        


        ranks_with_pairs = {rank: rank_count 
                            for rank, rank_count in self._card_rank_counts.items() 
                            if rank_count == 2}

        if len(ranks_with_pairs) == 1:
            return "Pair"
        if len(ranks_with_pairs) == 2:
            return "Two Pair"
            






        return "High Card"
    
    @property
    def _card_rank_counts(self) -> dict:
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


