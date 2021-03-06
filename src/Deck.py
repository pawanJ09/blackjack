import src.globals as g
from src.Card import Card
from random import shuffle
from itertools import product


class Deck:
    all_cards = []

    def __init__(self, deck_count):
        self.deck_count = deck_count
        cards_combo = list(product(g.suit, g.card_range))*deck_count
        for c in cards_combo:
            card = Card(c[0], c[1])
            self.all_cards.append(card)

    def __str__(self):
        return '\n'.join([str(card) for card in self.all_cards])

    def pop_one(self):
        return self.all_cards.pop(0)

    def shuffle_deck(self):
        shuffle(self.all_cards)

