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
    
    def test_figues_out_flush_is_the_best_rank(self):
        cards = [
            Card(rank= "Ace", suit= "Hearts"),
            Card(rank= "2", suit= "Hearts"),
            Card(rank= "5", suit= "Hearts"),
            Card(rank= "8", suit= "Hearts"),
            Card(rank= "7", suit= "Hearts"),
                 ]

        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), 
                         "Flush")

    def test_figues_out_full_house_is_the_best_rank(self):
        cards = [
            Card(rank= "5", suit= "Diamonds"),
            Card(rank= "5", suit= "Hearts"),
            Card(rank= "5", suit= "Spades"),
            Card(rank= "8", suit= "Spades"),
            Card(rank= "8", suit= "Clubs"),
                 ]

        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), 
                         "Full House")
    
    def test_figues_out_four_of_a_kind_is_the_best_rank(self):
        cards = [
            Card(rank= "5", suit= "Diamonds"),
            Card(rank= "5", suit= "Hearts"),
            Card(rank= "5", suit= "Spades"),
            Card(rank= "5", suit= "Clubs"),
            Card(rank= "8", suit= "Clubs"),
                 ]

        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), 
                         "Four of A Kind")

    def test_figues_out_straight_flush_is_the_best_rank(self):
        cards = [
            Card(rank= "3", suit= "Clubs"),
            Card(rank= "4", suit= "Clubs"),
            Card(rank= "5", suit= "Clubs"),
            Card(rank= "6", suit= "Clubs"),
            Card(rank= "7", suit= "Clubs"),
                 ]

        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), 
                         "Straight Flush")










if __name__ == "__main__":
    unittest.main()