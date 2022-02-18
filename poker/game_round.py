from typing import List


from poker.deck import Deck
from poker.player import Player
from poker.card import Card


class GameRound:
    def __init__(self, deck: Deck, players: List[Player]) -> None:
        self.deck = deck
        self.players = players

    def play(self) -> None:
        self._shuffle_deck()
        self._deal_initial_two_cards_from_deck_to_each_player()

    def _shuffle_deck(self) -> None:
        self.deck.shuffle()

    def _deal_initial_two_cards_from_deck_to_each_player(self) -> None:
        for each_player in self.players:
            two_cards: List[Card] = self.deck.remove_cards(2)
            each_player.add_cards(two_cards)
