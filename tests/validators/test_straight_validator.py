
import unittest
from poker.card import Card
from poker.validators import StraightValidator


class StraightValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        two           = Card(rank = "2", suit = "Spades")
        six           = Card(rank="6", suit="Hearts")
        self.seven    = Card(rank="7", suit="Spades")
        self.eight    = Card(rank="8", suit="Hearts")
        self.nine     = Card(rank="9", suit="Spades")
        self.ten      = Card(rank="10", suit="Diamonds")
        self.jack     = Card(rank= "Jack", suit= "Hearts")

        self.cards    = [
          two,six, self.seven, self.eight, self.nine, self.ten, self.jack
            
        ]

        
    def test_validates_that_cards_have_a_straight(self):

        validator = StraightValidator(cards = self.cards)
        self.assertEqual(validator.is_valid(),
                        True)


    def test_returns_five_highest_straight_cards_from_card_collection(self):
        

        validator = StraightValidator(cards= self.cards)

        self.assertEqual(
            validator.valid_cards(),
            self.cards[-5:]
        )

        

        

  
