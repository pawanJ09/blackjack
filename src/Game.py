from Card import Card
from Deck import Deck
from Player import Player
import globals as g


class Game:

    def __init__(self, deck=None, players=None):
        if players is None:
            players = []
        self.deck = deck
        self.players = players

    def setup_game(self):
        """
        This method invokes helper methods to initialize the deck, players, deal the cards
        """
        self.set_deck_and_players()
        self.set_dealer()
        self.deck.shuffle_deck()
        self.deal()
        pass

    def stop(self):
        pass

    def scores(self):
        pass

    def deal(self):
        """
        This method will deal 2 cards to each player from the created deck
        """
        for player in self.players:
            player_cards = []
            for i in range(2):
                player_cards.append(self.deck.pop_one())
            player.cards = player_cards

    def set_deck_and_players(self):
        """
        This method will initialize the playing deck and players
        """
        num_players = 0
        num_deck = 0
        while True:
            try:
                num_players = int(input('How many players would like to play this game? '))
                num_deck = int(input('How many decks would you like to play with? '))
            except ValueError as error:
                print('Please enter a valid number between 1-9')
                continue
            else:
                if num_players == 0 or num_deck == 0:
                    print('Please enter a valid number between 1-9')
                    continue
                break
        for np in range(num_players):
            player_name = input(f'Enter {np + 1} player name: ')
            player = Player(player_name)
            self.players.append(player)
        self.deck = Deck(num_deck)

    def set_dealer(self):
        """
        This method initializes the dealer as player to the game
        """
        player = Player("Dealer")
        self.players.append(player)

    def __str__(self):
        """
        Using string.format() because f strings don't allow backslashes
        :return: string
        """
        return 'Game stats ==> \n{}'.format("\n".join([str(player) for player in self.players]))


if __name__ == '__main__':
    game = Game()
    game.setup_game()
    print(game)
