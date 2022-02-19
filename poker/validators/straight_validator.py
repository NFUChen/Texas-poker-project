
from typing import List
from poker.card import Card

class StraightValidator:
    def __init__(self, cards:List[Card]) -> None:
        self._cards = cards
        self._name = "Straight"


    
    def is_valid(self) -> bool:
        # becomes optional, since self.__every_element_increasing_by_1 will do the check for us
        # if len(self._cards) < 5: 
        #     return False

        collections_of_valid_straight_cards = self._get_collections_of_valid_straight_cards()

        

        return len(collections_of_valid_straight_cards) >= 1

    
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

            curr_idx +=1

        return collections_of_valid_straight_cards
        
        
        

    def _every_element_increasing_by_1(self, rank_indexes) -> bool:

        return rank_indexes == list(range(rank_indexes[0], 
                                          rank_indexes[-1] + 1))



    def valid_cards(self) -> List[Card]:
        collections_of_valid_straight_cards:List[List[Card]] = self._get_collections_of_valid_straight_cards()
        highest_straight_cards:List[Card] = collections_of_valid_straight_cards[-1]
        return highest_straight_cards
        


        #return _valid_cards