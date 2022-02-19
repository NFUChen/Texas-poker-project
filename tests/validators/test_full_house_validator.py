
import unittest
from poker.card import Card
from poker.validators import FullHouseValidator


class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.five_of_diamonds = Card(rank="5", suit="Diamonds")
        self.five_of_hearts = Card(rank="5", suit="Hearts")
        self.five_of_spades = Card(rank="5", suit="Spades")
        self.eight_of_spades = Card(rank="8", suit="Spades")
        self.eight_of_clubs = Card(rank="8", suit="Clubs")

        self.cards = [
            self.five_of_diamonds,
            self.five_of_hearts,
            self.five_of_spades,
            Card(rank="3", suit="Diamonds"),
            self.eight_of_spades,
            self.eight_of_clubs,
            Card(rank="Queen", suit="Spades")

        ]

    def test_validates_that_cards_have_two_of_the_same_rank_and_three_of_another_rank(self):

        validator = FullHouseValidator(cards=self.cards)
        self.assertEqual(validator.is_valid(),
                         True)

    def test_returns_cards_having_two_of_the_same_rank_and_three_of_another_rank(self):

        validator = FullHouseValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.five_of_diamonds,
                self.five_of_hearts,
                self.five_of_spades,
                self.eight_of_clubs,
                self.eight_of_spades,


            ]
        )
