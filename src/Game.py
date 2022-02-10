from Card import Card
from Deck import Deck
from Player import Player
import globals as g
import os


def filter_winners(player):
    if player.cards_total <= 21:
        player.status = 'Winner !!'
        return True
    else:
        return False


def filter_losers(player):
    if player.cards_total > 21:
        player.status = 'Loser !!'
        return True
    else:
        return False


class Game:

    def __init__(self, deck=None, players=None):
        if players is None:
            players = []
        self.deck = deck
        self.players = players
        self.winners = []
        self.losers = []

    def play_game(self):
        """
        This method invokes helper methods to initialize the deck, players, deal the cards
        """
        self.set_deck_and_players()
        self.set_dealer()
        self.deck.shuffle_deck()
        self.deal()
        self.print_stats()
        self.start_game()
        self.start_dealer_game()
        self.evaluate_results()
        pass

    def stop(self):
        pass

    def print_stats(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Players ==> \n{}'.format("\n".join([str(player) for player in self.players
                                                   if player.player_name != "Dealer"])))

    def print_winners(self):
        print('Winners ==> \n{}'.format("\n".join([str(player) for player in self.winners])))

    def print_losers(self):
        print('Losers ==> \n{}'.format("\n".join([str(player) for player in self.losers])))

    def set_deck_and_players(self):
        """
        This method will initialize the playing deck and players
        """
        os.system('cls' if os.name == 'nt' else 'clear')
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

    def deal(self):
        """
        This method will deal 2 cards to each player from the created deck
        """
        for player in self.players:
            player_cards = []
            for i in range(2):
                player_cards.append(self.deck.pop_one())
            player.cards = player_cards
            for card in player.cards:
                player.cards_total += card.value

    def start_game(self):
        stay_list = list('H'*(len(self.players)-1))  # Doing -1 as not counting the dealer
        # Will only break if all players excluding the Dealer are at Stay
        while 'H' in stay_list:
            for count, player in enumerate(self.players):
                if player.player_name != "Dealer" and 'S' != stay_list[count]:
                    player_choice = input(f'{player.player_name} Press H to Hit and S to Stay: ')
                    if player_choice == 'H':
                        self.player_hit(player, stay_list, count)
                    else:
                        self.player_stay(player, stay_list, count)

    def player_hit(self, player, stay_list, count):
        """
        This method updates the player with the Hit card. If the Hit card is A and total goes
        above 21 then it considers value of A to be 1.
        Also, if total has reached 21 or above this will automatically update the player to Stay
        to avoid unnecessary hits.

        :param player: Player.Player object
        :param stay_list: String list with H or S elements
        :param count: Current loop counter for players
        """
        card = self.deck.pop_one()
        player.cards_total += card.value
        if player.cards_total > 21 and card.value == 11:
            card.value = 1
            player.cards_total -= 10
        if player.cards_total >= 21:
            stay_list[count] = 'S'
            if player.cards_total > 21:
                player.status = 'Busted !!'
        player.cards.append(card)
        self.print_stats()

    def player_stay(self, player, stay_list, count):
        """
        This method updates the status of the player when Stay is selected.

        :param player: Player.Player object
        :param stay_list: String list with H or S elements
        :param count: Current loop counter for players
        """
        stay_list[count] = 'S'
        player.status = 'Stay'
        self.print_stats()

    def start_dealer_game(self):
        """
        This method plays for the dealer after all players have played their bets. This will hit
        the deck if the total of dealer's cards is less than 17 and will stay once the total
        exceeds 17.
        """
        dealer = self.players[-1]
        while dealer.cards_total < 17:
            card = self.deck.pop_one()
            dealer.cards_total += card.value
            if dealer.cards_total > 21 and card.value == 11:
                card.value = 1
                dealer.cards_total -= 10
            if dealer.cards_total >= 21:
                if dealer.cards_total > 21:
                    dealer.status = 'Busted !!'
                dealer.cards.append(card)
                break
            dealer.cards.append(card)
        else:
            dealer.status = 'Stay'

    def evaluate_results(self):
        """
        This method will filter the winners and losers using the filter method of Python.
        """
        self.players.sort(key=lambda p: p.cards_total, reverse=True)
        os.system('cls' if os.name == 'nt' else 'clear')
        self.winners = filter(filter_winners, self.players)
        self.print_winners()
        self.losers = filter(filter_losers, self.players)
        self.print_losers()
        print(f'Total cards in deck {len(self.deck.all_cards)}')

    def __str__(self):
        """
        Using string.format() because f strings don't allow backslashes.

        :return: string
        """
        return 'Game stats ==> \n{}'.format("\n".join([str(player) for player in self.players]))


if __name__ == '__main__':
    game = Game()
    game.play_game()