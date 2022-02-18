from tkinter import N
from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound


def main():
    _52_cards = Card.generate_52_standard_cards()
    deck = Deck()
    deck.add_cards(_52_cards)
    hand1 = Hand()
    hand2 = Hand()
    hand1.add_cards([])
    hand2.add_cards([])
    player1 = Player(name="William", hand_obj=hand1)
    player2 = Player(name="Specter", hand_obj=hand2)

    game_round = GameRound(deck=deck, players=[player1, player2])

    game_round.play()

    print(player1.hand)
    print(player1.hand.cards)
    print(len(deck._cards))
    print(len(deck))


if __name__ == "__main__":
    main()
