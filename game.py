"""
Main file through which game will run. Contains game logic, exception handling and terminal I/O.
Author: Japjot Singh
"""
from helper import Deck, Hand
import sys, cmd

class Game:
    num_players = None
    deck_size = None

    deck = None

    def __init__(self, num_players, deck_size):
        self.num_players = num_players
        self.deck_size = deck_size
        self.deck = Deck(deck_size)


    def start(self):
        "Run the game and return the winner"
        # player_1 defaults to computer in 1 plyaer game
         player_1 = Hand()
         player_2 = Hand()
         while player_1.hand_value() < 22 and player_2.hand_value() < 22:


if __name__ == "__main__":
    valid_players = range(1, 10)
    valid_deck_size = range(1, 7)
    num_players = int(input("Number of Players [1 or 2]: "))
    deck_size = int(input("Deck Size [1-6]: "))
    if num_players not in valid_players or deck_size not in valid_deck_size:
        print("Inputted [Num Players: {}] [Deck Size: {}]".format(num_players, deck_size))
        print("======Invalid Game Parameters :( ======")
        sys.exit()
    print("Starting with [Num Players: {}] [Deck Size: {}]".format(num_players, deck_size))
    print("WELCOM TO BLACKJACK!\n")
    
    game = Game(num_players, deck_size)
    game.start()