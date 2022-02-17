from typing import List
class Card:
    '''
    Dummy Card class for type annotation
    '''
    pass

class Card:

    SUITS:tuple = ("Hearts","Clubs", "Spades", "Diamonds")
    RANKS:tuple = (
        "2", "3", "4", "5", "6", "7", "8", "9", "10", 
        "Jack", "Queen", "King", "Ace"
        )

    def __init__(self, rank:str, suit:str) -> None:
        if rank not in self.RANKS:
            raise ValueError(f"Please input valid rank. Rank must be one of the following {self.RANKS}")
        if suit not in self.SUITS:
            raise ValueError(f"Please input valid suit. Suit must be one of the following {self.SUITS}")
        self.rank = rank
        self.suit = suit

        self.rank_index = self.RANKS.index(self.rank)
        self.suit_index = self.SUITS.index(self.suit)

    


    @classmethod
    def generate_52_standard_cards(cls: Card) -> List[Card]:
        return [
            Card(suit= suit, rank= rank) 
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]

    def __eq__(self, __o: Card) -> bool:
        return (self.rank == __o.rank) and \
               (self.suit == __o.suit)

    def __gt__(self, __o: Card) -> bool:
        '''
        implement Card.sort() automatically
        '''
        

        return self.rank_index > __o.rank_index

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"


    def __repr__(self) -> str:
        return f"Card ('{self.rank}', '{self.suit}')"


