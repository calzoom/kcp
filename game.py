"""
Main file through which game will run. Contains game logic, exception handling and terminal I/O.
Author: Japjot Singh
"""
import helper
import sys, cmd

class Game:
    num_players = None
    deck_size = None

    def __init__(self, num_players, deck_size):
        self.num_players = num_players
        self.deck_size = deck_size

    def start(self, )

if __name__ == "__main__":
    valid_players = range(1, 10)
    valid_deck_size = range(1, 7)
    num_players = int(input("Numer of Players [1-9]: "))
    deck_size = int(input("Deck Size [1-6]: "))
    if num_players not in valid_players or deck_size not in valid_deck_size:
        print("Inputted [Num Players: {}] [Deck Size: {}]".format(num_players, deck_size))
        print("======Invalid Game Parameters :( ======")
        sys.exit()
    print("Starting with [Num Players: {}] [Deck Size: {}]".format(num_players, deck_size))
    
    game = Game(num_players, deck_size)

    print("Running Main")