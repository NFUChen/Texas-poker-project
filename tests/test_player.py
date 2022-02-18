
import unittest
from unittest.mock import MagicMock

from poker.card import Card
from poker.player import Player
from poker.hand import Hand


class PlayerTest(unittest.TestCase):
    def tests_stores_name_and_hand(self):
        hand = Hand()
        player = Player(name="PlayerName", hand_obj=hand)
        self.assertEqual(player.name, "PlayerName")
        self.assertEqual(player.hand, hand)

    def tests_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"
        player = Player(name="PlayerName", hand_obj=mock_hand)

        self.assertEqual(
            player.best_hand(), "Straight Flush"
        )

    def tests_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name="PlayerName", hand_obj=mock_hand)

        cards = [
            Card(rank="Ace", suit="Spades"),
            Card(rank="Queen", suit="Diamonds")
        ]

        player.add_cards(cards)

        mock_hand.add_cards.assert_called_once_with(cards)

        # mock_hand.best_rank.assert_called()

    def tests_decide_to_continue_or_drop_out_of_game(self):

        player = Player(name="PlayerName", hand_obj=Hand())
        self.assertEqual(
            player.wants_to_fold(), False
        )
