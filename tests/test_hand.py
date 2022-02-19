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


if __name__ == "__main__":
    unittest.main()
