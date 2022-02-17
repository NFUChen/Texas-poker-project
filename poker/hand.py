
from typing import List
from poker.card import Card


class Hand:
    def __init__(self, cards:List[Card]) -> None:
        self.cards = cards

    def best_rank(self) -> str:
        card_rank_count = {}
        for card in self.cards:
            card_rank_count.setdefault(card.rank, 0) # if the key already exists, do nothing
            card_rank_count[card.rank] += 1

        for rank_count in  card_rank_count.values():
            if rank_count == 2:
                return "Pair"
            






        return "High Card"

    


