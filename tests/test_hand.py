import unittest
from poker.card import Card
from poker.hand import Hand


class HandTest(unittest.TestCase):
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_cards_in_technical_representation(self):
        cards = [
            Card(rank="4", suit="Hearts"),
            Card(rank="Ace", suit="Diamonds"),
        ]
        hand = Hand()
        hand.add_cards(cards=cards)

        self.assertEqual(
            repr(hand),
            "4 of Hearts, Ace of Diamonds"
        )

    def test_receives_and_stores_cards(self):
        cards = [
            Card(rank="4", suit="Hearts"),
            Card(rank="Ace", suit="Hearts"),
        ]

        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(hand.cards, cards)

    def test_figues_out_straight_flush_is_the_best_rank(self):
        cards = [
            Card(rank="3", suit="Clubs"),
            Card(rank="4", suit="Clubs"),
            Card(rank="5", suit="Clubs"),
            Card(rank="6", suit="Clubs"),
            Card(rank="7", suit="Clubs"),
        ]

        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(hand.best_rank(),
                         "Straight Flush")

    def test_figues_out_royal_flush_is_the_best_rank(self):
        cards = [
            Card(rank="10", suit="Clubs"),
            Card(rank="Jack", suit="Clubs"),
            Card(rank="Queen", suit="Clubs"),
            Card(rank="King", suit="Clubs"),
            Card(rank="Ace", suit="Clubs"),
        ]

        hand = Hand()
        hand.add_cards(cards=cards)
        self.assertEqual(hand.best_rank(),
                         "Royal FLush")


if __name__ == "__main__":
    unittest.main()
