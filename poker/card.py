from re import L
from typing import List 


class Card:

    SUITS:tuple = ("Hearts","Clubs", "Spades", "Diamonds")
    RANKS:tuple = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

    def __init__(self, rank:str, suit:str):
        if rank not in self.RANKS:
            raise ValueError(f"Please input valid rank. \
                               Rank must be one of the following {self.RANKS}")
        if suit not in self.SUITS:
            raise ValueError(f"Please input valid suit. \
                               Suit must be one of the following {self.SUITS}")
        self.rank = rank
        self.suit = suit

    




    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"


    def __repr__(self) -> str:
        return f"Card ('{self.rank}', '{self.suit}')"
