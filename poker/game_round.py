from typing import List


from poker.deck import Deck
from poker.player import Player


class GameRound:
    def __init__(self, deck: Deck, players: List[Player]) -> None:
        self.deck = deck
        self.players = players
        self.number_of_players_in_game = len(players)

    def play(self):
        self.deck.shuffle()

        for each_game in range(self.number_of_players_in_game):
            self.deck.remove_cards(2)

        # for player in self.players:
        #     self.deck.remove_cards(2)
