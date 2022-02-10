import globals as g


class Card:

    def __init__(self, suit, name):
        self.name = name
        self.suit = suit
        self.value = g.card_range[name]

    def __str__(self):
        return f'{g.card_range_symbols[self.name]}{g.suits_symbols[self.suit]}'


if __name__ == '__main__':
    c = Card("Diamonds", "Seven")
    print(c)