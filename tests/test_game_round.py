from operator import ne
import unittest
from unittest.mock import MagicMock, call


from poker.game_round import GameRound
from poker.card import Card
from poker.player import Player


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

        first_two_cards = [
            Card(rank="2", suit="Hearts"),
            Card(rank="6", suit="Spades")
        ]

        next_two_cards = [
            Card(rank="9", suit="Diamonds"),
            Card(rank="4", suit="Spades")
        ]

        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            first_two_cards,  # first time call
            next_two_cards  # second time call
        ]

        mock_player1 = MagicMock()
        mock_player2 = MagicMock()

        mock_players = [
            mock_player1, mock_player2
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

        mock_player1.add_cards.assert_called_with(first_two_cards)
        mock_player2.add_cards.assert_called_with(next_two_cards)

    def test_removes_player_if_not_willing_to_make_bet(self):
        mock_deck = MagicMock()
        player1 = MagicMock()
        player2 = MagicMock()

        player1.wants_to_fold.return_value = True  # player1 wants to fold
        player2.wants_to_fold.return_value = False  # player2 doesn't want to fold

        mock_players = [player1, player2]

        game_round = GameRound(deck=mock_deck,
                               players=mock_players)

        game_round.play()

        self.assertEqual(
            game_round.players, [player2]
        )
