from poker.card import Card

def main():
    card1 = Card("2", "Hearts")
    print(card1)
    _52_cards = cards = Card.generate_52_standard_cards()
    print(_52_cards)




if __name__ == "__main__":
    main()