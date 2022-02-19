import unittest
from poker.card import Card
from poker.validators import PairValidator


class PairValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_exactly_one_pair(self):
          cards = [
              Card(rank="Ace", suit="Hearts"),
              Card(rank="Ace", suit="Spades")
          ]

          validator = PairValidator(cards= cards)
          self.assertEqual(validator.is_valid(),
                          True)


    def test_returns_pair_cards_from_card_collection(self):
        

        ten_of_hearts = Card(rank="10", suit="Hearts")
        ten_of_spades = Card(rank="10", suit="Spades")

        cards = [
            Card(rank="3", suit="Hearts"),
            Card(rank="5", suit="Spades"),
            Card(rank= "King", suit= "Clubs"),
            ten_of_spades,
            ten_of_hearts, 
        ]

        validator = PairValidator(cards= cards)

        self.assertEqual(
            validator.valid_cards(),
            [ten_of_spades, ten_of_hearts]
        )