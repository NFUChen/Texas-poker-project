import unittest
from unittest.mock import MagicMock, call


from poker.game_round import GameRound


class GameRoundTest(unittest.TestCase):
    def tests_stores_deck_and_players(self):
        deck = MagicMock()
        mock_players = [
            MagicMock(),
            MagicMock()
        ]
        game_round = GameRound(deck=deck,
                               players=mock_players)

        self.assertEqual(game_round.players, mock_players)

    def tests_game_play_shuffle_deck(self):
        mock_deck = MagicMock()
        mock_players = [
            MagicMock(),
            MagicMock()
        ]
        game_round = GameRound(deck=mock_deck,
                               players=mock_players)

        game_round.play()
        mock_deck.shuffle.assert_called_once()

    def tests_deals_two_initial_cards_from_deck_to_each_player(self):
        mock_deck = MagicMock()
        mock_players = [
            MagicMock(),
            MagicMock()
        ]
        game_round = GameRound(deck=mock_deck,
                               players=mock_players)

        game_round.play()

        mock_deck.remove_cards.assert_has_calls([
            # tests if deck.removed_cards() calls twice
            # with argument 2(i.e., number:int),
            # meaning that the GameRound class will deal two cards for two times
            call(2), call(2)

        ])
