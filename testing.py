"""
Contains unit tests for Blackjack game
Author: Japjot Singh
"""
import unittest
from helper import Card, Deck

class TestCard(unittest.TestCase):
    def test_rank_suit_vals(self):
        self.assertRaises(ValueError, Card, 14, "Spade")
        self.assertRaises(ValueError, Card, None, "Spade")
        self.assertRaises(ValueError, Card, "fourteen", "Spade")
        self.assertRaises(ValueError, Card, 14, "King")
        self.assertRaises(ValueError, Card, 6, None)
        self.assertRaises(ValueError, Card, None, 29)
        Card(12, "Spade"), Card(9, "Heart"), Card(1, "Diamond")
        print("Card Init: PASSED")

    def test_card_vals(self):
        a, b, c, d = Card(12, "Spade"), Card(9, "Heart"), Card(1, "Diamond"), Card(13, "Clover")
        self.assertEqual(a.get_value()[0], 10)
        self.assertEqual(b.get_value()[0], 9)
        self.assertEqual(c.get_value()[0], 1)
        self.assertEqual(c.get_value()[1], 11)
        self.assertEqual(d.get_value()[0], 10)
        print("Card Values: PASSED")

class TestDeck(unittest.TestCase):
    def test_deck_init(self):
        self.assertRaises(ValueError, Deck, 0)
        self.assertRaises(ValueError, Deck, -1)
        self.assertRaises(ValueError, Deck, 14)
        self.assertRaises(ValueError, Deck, "Yes")
        self.assertRaises(ValueError, Deck, None)
        a, b, c = Deck(), Deck(2), Deck(6)
        self.assertEqual(a.num_decks, 1)
        self.assertEqual(b.num_decks, 2)
        self.assertEqual(c.num_decks, 6)
        self.assertEqual(a.num_cards, 52)
        self.assertEqual(b.num_cards, 52*2)
        self.assertEqual(c.num_cards, 52*6)
        print("Deck Init: PASSED")
    
    def test_shuffle(self):
        a, b = Deck(), Deck(6)
        a.shuffle()
        b.shuffle()
        self.assertEqual(len(a.my_deck), len(a.my_deck), "shuffling the deck should not change its size")
        self.assertEqual(len(b.my_deck), len(b.my_deck), "shuffling the deck should not change its size")

# class TestGame(unittest.TestCase):
#     def test_game_init(self):
            

if __name__ == "__main__":
    print("Running: Testing.py -----")
    unittest.main()
