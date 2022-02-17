
from typing import Callable, List, Tuple
from poker.card import Card
    

class Hand:
    def __init__(self, cards:List[Card]) -> None:
        copy = cards[:]
        copy.sort()
        self.cards = copy

    

    @property
    def _rank_validations_from_best_to_worst(self) -> Tuple[Tuple[str, Callable]]:
        '''
        Helper property of .best_rank() method, 
        which the returned tuple (which will be unpacked as well) will be iterated over, 
        '''
        return (
        ("Straight", self._straight),
        ("Three of A Kind", self._three_of_a_kind),
        ("Two Pair", self._two_pair),
        ("Pair", self._pair),
        ("High Card",self._high_card),
        
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

    


        
            




    def _straight(self) -> bool:
        rank_indexes = [card.rank_index for card in self.cards]
        #e.g., rank_indexes = [6,7,8,9,10] 
        # rank_indexes== list(range(6, 11))
        return rank_indexes == list(range(rank_indexes[0],rank_indexes[-1] + 1))
        

    
    def _three_of_a_kind(self) -> bool:
        '''
        Test if current hand has three of a a kind.
        '''
        ranks_with_three_of_a_kind = self._ranks_with_target_count(3)
        return len(ranks_with_three_of_a_kind) == 1

    def _two_pair(self) -> bool:
        '''
        Test if current hand has two pair.
        '''
        ranks_with_pairs = self._ranks_with_target_count(2)
        return len(ranks_with_pairs) == 2

    def _pair(self) -> bool:
        '''
        Test if current hand has pair.
        '''
        ranks_with_pair = self._ranks_with_target_count(2)
        return len(ranks_with_pair) == 1

    def _high_card(self) -> bool:
        '''
        Test if current hand has high card.
        '''
        return True

    
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


