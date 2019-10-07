"""
Contains utility functions / data structures and objects for this game.
Author: Japjot Singh
"""
import unittest
import random
from collections import deque

class Card:
    """
    Every card has a rank and suit, rank must either be a number in [1, 13]
    where Ace is 1, Jack is 11, Queen is 12, and King is 13
    """
    suits = ("Spade", "Clover", "Heart", "Diamond")
    ranks = list(range(1, 14))
    rank = None
    suit = None

    def __init__(self, rank, suit):
        if rank not in self.ranks or suit not in self.suits: 
            raise ValueError("Invaild Card initialization: [Rank:{} Suit:{}]".format(rank, suit))
        self.rank = rank
        self.suit = suit

    def get_value(self):
        """
        Return the value of this card as a list
        """
        if self.rank == 1:
            # an ace is worth 1 or 11
            return tuple([1, 11])
        elif self.rank > 10:
            return tuple([10])
        else:
            return tuple([self.rank])

class Deck:
    # based off casino rules you can use up to 6-decks
    cards_in_single_deck = 52
    num_decks = None
    num_cards = None

    # these values will change 
    my_deck = None
    discard_pile = None
    cards_remaining = None

    def __init__(self, num_decks=1):
        if num_decks not in range(1, 7):
            raise ValueError("Invalid Deck Size of {}".format(num_decks))

        self.num_decks = num_decks
        self.num_cards = self.num_decks * self.cards_in_single_deck

        self.init_deck()
    
    def shuffle(self):
        random.shuffle(self.my_deck)

    def init_deck(self):
        self.my_deck = deque([])
        self.discard_pile = []

        for _ in range(self.num_decks):
            for suit in Card.suits:
                for rank in Card.ranks:
                    self.my_deck.append(Card(rank, suit))

        self.shuffle()
        self.cards_remaining = self.num_cards
    
    def deal(self):
        """
        If there are no cards remaining, shuffle the discard pile, empty it, and update new variables
        Return the card at the top of the deck, put it in this discard pile, and decrement cards_remaining
        """
        if self.cards_remaining == 0:
            self.init_deck()

        card = self.my_deck.popleft()
        self.discard_pile.append(card)

        self.cards_remaining -= 1

        return card

    def read_deck(self):
        for card in self.my_deck:
            print("here")
            print("{}\n".format((card.rank, card.suit)))

    def read_values(self):
        for card in self.my_deck:
            print(card.rank)

if __name__ == "__main__":
    d = Deck()
    for _ in range(1000):
        print(d.deal().rank)
    print("running helper.py main")