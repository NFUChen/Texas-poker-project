
import unittest
from poker.card import Card
from poker.validators import ThreeOfAKindValidator


class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        ten_of_hearts = Card(rank="10", suit="Hearts")
        ten_of_spades = Card(rank="10", suit="Spades")
        self.five_of_hearts = Card(rank="5", suit="Hearts")
        self.five_of_spades = Card(rank="5", suit="Spades")
        self.five_of_clubs = Card(rank= "5", suit= "Clubs")

        self.cards = [
            self.five_of_clubs,
            self.five_of_hearts,
            self.five_of_spades,
            ten_of_spades,
            ten_of_hearts, 
        ]

    def test_validates_that_cards_have_a_three_of_a_kind(self):

        validator = ThreeOfAKindValidator(cards = self.cards)
        self.assertEqual(validator.is_valid(),
                        True)


    def test_returns_three_of_a_kind_cards_from_card_collection(self):
        

        validator = ThreeOfAKindValidator(cards= self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
              self.five_of_clubs,
              self.five_of_hearts,
              self.five_of_spades,
            ] 
        )

        

