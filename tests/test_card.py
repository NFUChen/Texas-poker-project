import unittest
from poker.card import Card


class CardTest(unittest.TestCase):
    def test_has_rank_and_suit(self):
        test_card = Card(rank="Queen", suit="Hearts")
        self.assertEqual(test_card.rank, "Queen")
        self.assertEqual(test_card.suit, "Hearts")

    def test_has_rank_and_suit_index(self):
        test_card = Card(rank="Jack", suit="Hearts")
        self.assertEqual(test_card.rank_index, 9)
        self.assertEqual(test_card.suit_index, 0)

    def test_has_string_representation_with_rank_and_suit(self):
        """
        implementation of __str__() method in Card class
        """
        test_card = Card(rank="5", suit="Hearts")
        self.assertEqual(str(test_card), "5 of Hearts")

    def test_has_technical_representation(self):
        """
        implementation of __repr__() method in Card class
        """
        test_card = Card(rank="5", suit="Hearts")
        self.assertEqual(repr(test_card), "Card ('5', 'Hearts')")

    def test_has_four_possible_suit_options(self):

        self.assertEqual(len(Card.SUITS), 4)
        self.assertEqual(Card.SUITS,
                         ("Hearts", "Clubs", "Spades", "Diamonds"))

    def test_has_thirteen_possible_rank_options(self):

        self.assertEqual(len(Card.RANKS), 13)
        self.assertEqual(Card.RANKS,
                         ("2", "3", "4", "5", "6", "7", "8", "9", "10",
                          "Jack", "Queen", "King", "Ace"))

    def test_card_only_allows_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank="Two", suit="Hearts")

    def test_card_only_allows_for_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank="2", suit="Heart")

    def test_card_class_can_generate_52_standard_cards(self):
        _52_cards = Card.generate_52_standard_cards()
        self.assertEqual(len(_52_cards), 52)
        # need to implement __eq__ to pass the test
        self.assertEqual(_52_cards[0], Card(rank="2", suit="Hearts"))
        self.assertEqual(_52_cards[-1], Card(rank="Ace", suit="Diamonds"))

    def test_figures_out_if_two_cards_are_equal(self):
        test_card1 = Card(rank="Queen", suit="Hearts")
        test_card2 = Card(rank="Queen", suit="Hearts")
        self.assertTrue(test_card1 == test_card2)

    def test_figures_out_if_one_card_is_greater_than_other_card(self):
        two_of_spades = Card(rank="2", suit="Spades")
        five_of_hearts = Card(rank="5", suit="Hearts")
        self.assertTrue(five_of_hearts > two_of_spades)

        queen_of_spades = Card(rank="Queen", suit="Spades")
        king_of_spades = Card(rank="King", suit="Spades")
        self.assertTrue(king_of_spades > queen_of_spades,
                        "No comparison concept implemented")

    def test_sorts_cards(self):
        two_of_spades = Card(rank="2", suit="Spades")
        five_of_diamonds = Card(rank="5", suit="Diamonds")
        five_of_hearts = Card(rank="5", suit="Hearts")
        eight_of_hearts = Card(rank="8", suit="Hearts")
        ace_of_clubs = Card(rank="Ace", suit="Clubs")

        unsorted_cards = [
            eight_of_hearts,
            ace_of_clubs,
            two_of_spades,
            five_of_hearts,
            five_of_diamonds,
            

        ]
        unsorted_cards.sort()
        self.assertEqual(unsorted_cards,
                         [
                             two_of_spades,
                             five_of_diamonds,
                             five_of_hearts,
                             eight_of_hearts,
                             ace_of_clubs
                         ])


if __name__ == "__main__":
    unittest.main()
