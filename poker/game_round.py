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
        
        self._make_bets()
        self._deal_flop_cards()

        self._deal_turn_card()
        self._make_bets()

        self._deal_river_card()
        self._make_bets()


    def _shuffle_deck(self) -> None:
        self.deck.shuffle()

    def _deal_initial_two_cards_from_deck_to_each_player(self) -> None:
        for current_player in self.players:
            two_cards: List[Card] = self.deck.remove_cards(2)
            current_player.add_cards(two_cards)

    def _make_bets(self) -> None:
        for current_player in self.players:
            if current_player.wants_to_fold():
                self.players.remove(current_player)

    def _deal_flop_cards(self) -> None:
        community_cards:List[Card] = self.deck.remove_cards(3)
        for current_player in self.players:
            current_player.add_cards(community_cards)

    def _deal_turn_card(self) -> None:
        community_card:List[Card] = self.deck.remove_cards(1)
        for current_player in self.players:
            current_player.add_cards(community_card)

    def _deal_river_card(self) -> None:
        community_card:List[Card] = self.deck.remove_cards(1)
        for current_player in self.players:
            current_player.add_cards(community_card)

        
