from unittest import TestCase
import unittest
from poker.deck import Deck
from poker.card import Card


class DeckTest(unittest.TestCase):
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(deck._cards, [])

    def test_add_cards_to_its_collection(self):
        card1 = Card(rank= "Queen", suit = "Hearts")
        card2 = Card(rank= "Queen", suit = "Spades")
        deck = Deck()
        deck.add_cards([card1, card2])
        self.assertEqual(deck._cards, [card1, card2])





if __name__ == "__main__":
    unittest.main()
