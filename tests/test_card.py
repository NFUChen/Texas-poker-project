import unittest
from poker.card import Card



    

class CardTest(unittest.TestCase):
    def test_has_rank_and_suit(self):
        test_card = Card(rank= "Queen", suit = "Hearts")
        self.assertEqual(test_card.rank, "Queen")
        self.assertEqual(test_card.suit, "Hearts")

    def test_has_string_representation_with_rank_and_suit(self):
        """
        implementation of __str__() method in Card class
        """
        test_card = Card(rank= "5", suit = "Hearts")
        self.assertEqual(str(test_card),"5 of Hearts")
    

    def test_has_technical_representation(self):
        """
        implementation of __repr__() method in Card class
        """
        test_card = Card(rank= "5", suit = "Hearts")
        self.assertEqual(repr(test_card),"Card ('5', 'Hearts')")

    def test_has_four_possible_suit_options(self):

        self.assertEqual(len(Card.SUITS),4)
        self.assertEqual(Card.SUITS, 
                        ("Hearts","Clubs", "Spades", "Diamonds"))

    def test_has_thirteen_possible_rank_options(self):

        self.assertEqual(len(Card.RANKS),13)
        self.assertEqual(Card.RANKS, 
                        ("2", "3", "4", "5", "6", "7", "8", "9", "10", 
                        "Jack", "Queen", "King", "Ace"))

    def test_card_only_allows_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit="Hearts")

    def test_card_only_allows_for_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank = "2", suit="Heart")


    def test_card_class_can_generate_52_standard_cards(self):
        _52_cards = Card.generate_52_standard_cards()
        self.assertEqual(len(_52_cards), 52)
        # need to implement __eq__ to pass the test
        self.assertEqual(_52_cards[0], Card(rank = "2", suit= "Hearts"))
        self.assertEqual(_52_cards[-1], Card(rank = "Ace", suit= "Diamonds")) 

    def test_figures_out_if_two_cards_are_equal(self):
        test_card1 = Card(rank= "Queen", suit = "Hearts")
        test_card2 = Card(rank= "Queen", suit = "Hearts")
        self.assertTrue(test_card1 == test_card2)

    

if __name__ == "__main__":
    unittest.main()