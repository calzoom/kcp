"""
Main file through which game will run. Contains game logic, exception handling and terminal I/O.
Author: Japjot Singh
"""
from helper import Deck, Hand
import sys, cmd
import random

class Game:
    deck_size = None

    deck = Deck()

    def __init__(self, deck_size):
        self.deck_size = deck_size
        self.deck = Deck(deck_size)

    def deal_card(self):
        return self.deck.deal()
    
    def query_play_again(self):
        pg = int(input("Play again? 1 for Yes 0 for No: "))
        if pg:
            return True
        return False

    def start(self):
        "Run the game and return the winner"

        play = True

        while play:
            dealer = Hand()
            player = Hand()
            while dealer.hand_value() < 22 and player.hand_value() < 22:
                hit_2 = int(input("Enter 0 to Stand or 1 to Hit: "))
                dealer_strat = random.randint(0, 1)

                if dealer_strat:
                    print("Dealer Hit...")
                else:
                    print("Dealer Stand...")

                if dealer_strat:
                    dealer.add_card(self.deal_card())
                
                if hit_2:
                    player.add_card(self.deal_card())
                
                print("Hand: {}".format(player.get_hand()))

                print("P1: {} P2: {}".format(dealer.hand_value(), player.hand_value()))
            
            if dealer.hand_value() >= 22:
                print("You WON!!!\n")

            else:
                print("Lost Game...\n")
            
            play = self.query_play_again()
            



if __name__ == "__main__":
    valid_players = range(1, 10)
    valid_deck_size = range(1, 7)
    deck_size = int(input("Deck Size [1-6]: "))
    if deck_size not in valid_deck_size:
        print("Inputted [Deck Size: {}]".format(deck_size))
        print("======Invalid Game Parameters :( ======")
        sys.exit()
    print("Starting with [Deck Size: {}]".format(deck_size))
    print("WELCOM TO BLACKJACK!\n")
    
    game = Game(deck_size)
    game.start()