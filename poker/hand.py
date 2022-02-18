
from typing import Callable, List, Tuple
from poker.card import Card
    

class Hand:
    def __init__(self, cards:List[Card]) -> None:
        copy = cards[:]
        copy.sort()
        self.cards = copy
        self.amount_of_cards_hold = len(self.cards)

    

    @property 
    def _rank_validations_from_best_to_worst(self) -> Tuple[Tuple[str, Callable]]:
        '''
        Helper property of .best_rank() method, 
        which the returned tuple (which will be unpacked as well) will be iterated over, 
        '''
        return (
        ("Royal FLush", self._royal_flush),
        ("Straight Flush", self._straight_flush),
        ("Four of A Kind", self._four_of_a_kind),
        ("Full House", self._full_house),
        ("Flush", self._flush),
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

    
    def _royal_flush(self) -> bool:
        is_straight_flush = self._straight_flush()

        is_royal = (self.cards[-1].rank == "Ace" and 
                    self.cards[0].rank == "10")
                    
        return is_straight_flush and is_royal
    

    def _straight_flush(self) -> bool:
        return self._flush() and self._straight()

    
    def _four_of_a_kind(self) -> bool:
        '''
        Test if current hand has a four of a a kind.
        '''
        ranks_with_four_of_a_kind = self._ranks_with_target_count(4)
        return len(ranks_with_four_of_a_kind) == 1

    def _full_house(self) -> bool:
        return self._three_of_a_kind() and self._pair() 
    


    def _flush(self) -> bool:
        '''
        Test if current hand has a flush.
        '''
        suits_that_occur_5_or_more_times = {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5 }
        
        return len(suits_that_occur_5_or_more_times) == 1



    def _straight(self) -> bool:
        '''
        Test if current hand has a straight.
        '''
        rank_indexes = [card.rank_index for card in self.cards]
        #e.g., rank_indexes = [6,7,8,9,10] 
        # rank_indexes== list(range(6, 11))
        if self.amount_of_cards_hold < 5:
            return False

        return rank_indexes == list(range(rank_indexes[0],rank_indexes[-1] + 1))
        

    
    def _three_of_a_kind(self) -> bool:
        '''
        Test if current hand has a three of a a kind.
        '''
        ranks_with_three_of_a_kind = self._ranks_with_target_count(3)
        return len(ranks_with_three_of_a_kind) == 1

    def _two_pair(self) -> bool:
        '''
        Test if current hand has a two pair.
        '''
        ranks_with_pairs = self._ranks_with_target_count(2)
        return len(ranks_with_pairs) == 2

    def _pair(self) -> bool:
        '''
        Test if current hand has a pair.
        '''
        ranks_with_pair = self._ranks_with_target_count(2)
        return len(ranks_with_pair) == 1

    def _high_card(self) -> bool:
        '''
        Test if current hand has high cards.
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

    def _suits_with_target_count(self, target_count:int) -> dict:
        '''
        coupled with _card_rank_counts() method
        '''
        return {
            suit: suit_count 
            for suit, suit_count in self._card_suit_counts.items() 
            if suit_count == target_count ## >=
               }

    @property
    def _card_suit_counts(self) -> dict:
        card_suit_count = {}
        for card in self.cards:
            card_suit_count.setdefault(card.suit, 0) # if the key already exists, do nothing
            card_suit_count[card.suit] += 1

        return card_suit_count

    


