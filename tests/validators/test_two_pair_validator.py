import unittest
from poker.card import Card
from poker.validators import TwoPairValidator


class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.ten_of_hearts = Card(rank="10", suit="Hearts")
        self.ten_of_spades = Card(rank="10", suit="Spades")
        self.five_of_hearts = Card(rank="5", suit="Hearts")
        self.five_of_spades = Card(rank="5", suit="Spades")

        self.cards = [
            Card(rank= "King", suit= "Clubs"),
            self.five_of_hearts,
            self.five_of_spades,
            self.ten_of_spades,
            self.ten_of_hearts, 
        ]

    def test_validates_that_cards_have_at_least_two_pairs(self):

        validator = TwoPairValidator(cards = self.cards)
        self.assertEqual(validator.is_valid(),
                        True)


    def test_returns_two_pair_cards_from_card_collection(self):
        

        validator = TwoPairValidator(cards= self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [self.five_of_hearts,self.five_of_spades, #first_parir
            self.ten_of_spades,self.ten_of_hearts] #second_pair
        )

        