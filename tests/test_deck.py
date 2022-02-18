import unittest
from unittest.mock import patch

from poker.deck import Deck
from poker.card import Card


class DeckTest(unittest.TestCase):
    def test_has_length_that_is_equal_to_count_of_cards(self):
        deck = Deck()
        self.assertEqual(len(deck), 0)

    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(deck._cards, [])

    def test_add_cards_to_its_collection(self):
        card1 = Card(rank="Queen", suit="Hearts")
        card2 = Card(rank="Queen", suit="Spades")
        deck = Deck()
        deck.add_cards([card1, card2])
        self.assertEqual(deck._cards, [card1, card2])

    @patch("random.shuffle")
    def tests_shuffle_cards_in_random_order(self, mock_shuffle):
        deck = Deck()

        cards = [
            Card(rank="2", suit="Spades"),
            Card(rank="5", suit="Diamonds")
        ]
        deck.add_cards(cards)

        deck.shuffle()

        mock_shuffle.assert_called_once_with(cards)

    def tests_remove_specified_number_of_cards_from_deck(self):
        ace = Card(rank="Ace", suit="Spades"),
        eight = Card(rank="8", suit="Diamonds")
        cards = [ace, eight]
        deck = Deck()
        deck.add_cards(cards)

        # checks if .removed_cards() will return a list of cards being removed
        self.assertEqual(
            deck.remove_cards(1), [ace]
        )

        # checks if .removed_carsd() will truely modify the origin deck._cards attributes,
        # since .removed_cards() removes cards from it.
        self.assertEqual(deck._cards, [eight])


if __name__ == "__main__":
    unittest.main()
