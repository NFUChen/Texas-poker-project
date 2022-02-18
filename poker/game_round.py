from typing import List
from poker.deck import Deck
from poker.player import Player


class GameRound:
    def __init__(self, deck: Deck, players: List[Player]) -> None:
        self.deck = deck
        self.players = players

    def play(self):
        self.deck.shuffle()
