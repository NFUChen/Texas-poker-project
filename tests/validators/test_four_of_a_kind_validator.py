
import unittest
from poker.card import Card
from poker.validators import FourOfAKindValidator


class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self) -> None:

        self.five_of_diamonds = Card(rank="5", suit="Diamonds")
        self.five_of_hearts = Card(rank="5", suit="Hearts")
        self.five_of_spades = Card(rank="5", suit="Spades")
        self.five_of_clubs = Card(rank="5", suit="Clubs")

        self.cards = [
            Card(rank="2", suit="Clubs"),
            self.five_of_diamonds,
            self.five_of_hearts,
            self.five_of_spades,
            self.five_of_clubs,
            Card(rank="8", suit="Clubs"),
            Card(rank="7", suit="Spades")
        ]

    def test_validates_that_four_cards_of_one_rank_are_present(self):

        validator = FourOfAKindValidator(cards=self.cards)
        self.assertEqual(validator.is_valid(),
                         True)

    def test_returns_four_cards_with_the_same_rank(self):

        validator = FourOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.five_of_clubs,
                self.five_of_diamonds,
                self.five_of_hearts,
                self.five_of_spades,

            ]
        )
