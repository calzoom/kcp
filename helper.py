"""
Contains utility functions / data structures and objects for this game.
Author: Japjot Singh
"""
import unittest

class Card:
    """
    Every card has a rank and suit, rank must either be a number in [1, 13]
    where Ace is 1, Jack is 11, Queen is 12, and King is 13
    """
    rank = None
    suit = None
    def __init__(self, rank, suit):
        if rank not in range(1, 14) or suit not in ["Spade", "Clover", "Heart", "Diamond"]: 
            raise ValueError("Invaild Card initialization: [Rank:{} Suit:{}]".format(self.rank, self.suit))
        self.rank = rank
        self.suit = suit

    def get_value(self):
        """
        Return the value of this card as a list
        """
        if self.rank == 1:
            # an ace is worth 1 or 11
            return [1, 11]
        elif self.rank > 10:
            return [10]
        else:
            return [self.rank]



if __name__ == "__main__":
    a = Card("neck", "Spades")
    print("running helper.py main")