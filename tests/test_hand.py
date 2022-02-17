import unittest
from poker.card import Card
from poker.hand import Hand

class HandTest(unittest.TestCase):
    def test_receives_and_stores_cards(self):
        cards = [
            Card(rank= "4", suit= "Hearts"),
            Card(rank= "Ace", suit= "Hearts"),
                 ]
        
        hand = Hand(cards = cards)
        self.assertEqual(hand.cards, cards)

    def test_figues_out_high_card_is_the_best_rank(self):
        cards = [
            Card(rank= "6", suit= "Hearts"),
            Card(rank= "7", suit= "Spades")
                 ]

        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), 
                         "High Card")

    def test_figues_out_pair_is_the_best_rank(self):
        cards = [
            Card(rank= "Ace", suit= "Hearts"),
            Card(rank= "Ace", suit= "Spades")
                 ]

        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), 
                         "Pair")

    def test_figues_out_two_pairs_is_the_best_rank(self):
        cards = [
            Card(rank= "Ace", suit= "Hearts"),
            Card(rank= "Ace", suit= "Spades"),
            Card(rank= "7", suit= "Hearts"),
            Card(rank= "7", suit= "Spades"),
            Card(rank= "5", suit= "Spades")
                 ]

        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), 
                         "Two Pair")


    def test_figues_out_three_of_a_kind_is_the_best_rank(self):
        cards = [
            Card(rank= "Ace", suit= "Hearts"),
            Card(rank= "3", suit= "Spades"),
            Card(rank= "7", suit= "Hearts"),
            Card(rank= "7", suit= "Spades"),
            Card(rank= "7", suit= "Diamonds"),
                 ]

        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), 
                         "Three of A Kind")

    def test_figues_out_straight_of_a_kind_is_the_best_rank(self):
        cards = [
            Card(rank= "6", suit= "Hearts"),
            Card(rank= "7", suit= "Spades"),
            Card(rank= "8", suit= "Hearts"),
            Card(rank= "9", suit= "Spades"),
            Card(rank= "10", suit= "Diamonds"),
                 ]

        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), 
                         "Straight")










if __name__ == "__main__":
    unittest.main()