import unittest
from unittest.mock import MagicMock
from poker.game_round import GameRound


class GameRoundTest(unittest.TestCase):
    def tests_stores_deck_and_players(self):
        deck = MagicMock()
        players = [
            MagicMock(),
            MagicMock()
        ]
        game_round = GameRound(deck=deck,
                               players=players)

        self.assertEqual(game_round.players, players)

    def tests_game_play_shuffle_deck(self):
        mock_deck = MagicMock()
        players = [
            MagicMock(),
            MagicMock()
        ]
        game_round = GameRound(deck=mock_deck,
                               players=players)

        game_round.play()
        mock_deck.shuffle.assert_called_once()
