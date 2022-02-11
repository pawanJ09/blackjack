from src.Card import Card
from src.Deck import Deck


class Player:

    def __init__(self, player_name, cards=None):
        if cards is None:
            cards = []
        self.player_name = player_name
        self.cards = cards
        self.cards_total = 0
        self.status = 'In Game'

    def __str__(self):
        return f'{self.player_name} has {", ".join([str(card) for card in self.cards])}. ' \
               f'Total: {self.cards_total}. Status: {self.status}'
