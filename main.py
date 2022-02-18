from tkinter import N
from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player


def main():
    card1 = Card("2", "Hearts")
    print(card1)
    _52_cards = Card.generate_52_standard_cards()
    print(_52_cards)
    deck = Deck()
    deck.add_cards(_52_cards)
    hand1 = Hand()
    hand2 = Hand()
    hand1.add_cards([])
    hand2.add_cards([])
    player1 = Player(name="William", hand_obj=hand1)
    player2 = Player(name="Specter", hand_obj=hand2)

    player1.best_hand()


if __name__ == "__main__":
    main()
