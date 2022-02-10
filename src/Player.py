from Card import Card
from Deck import Deck


class Player:

    def __init__(self, player_name, cards=None):
        if cards is None:
            cards = []
        self.player_name = player_name
        self.cards = cards

    def __str__(self):
        return f'{self.player_name} has {", ".join([str(card) for card in self.cards])}'


if __name__ == '__main__':
    player_cards = []
    d = Deck(1)
    for i in range(2):
        player_cards.append(d.pop_one())
    p = Player("Pawan", player_cards)
    print(p)
