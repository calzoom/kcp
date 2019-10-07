"""
Contains unit tests for Blackjack game
Author: Japjot Singh
"""
import unittest
from helper import Card

class TestStringMethods(unittest.TestCase):
    def test_rank_suit_vals(self):
        self.assertRaises(ValueError, Card, 14, "Spades")
        self.assertRaises(ValueError, Card, None, "Spades")
        self.assertRaises(ValueError, Card, "fourteen", "Spades")
        self.assertRaises(ValueError, Card, 14, "Kings")
        self.assertRaises(ValueError, Card, 6, None)
        self.assertRaises(ValueError, Card, None, 29)

if __name__ == "__main__":
    print("Running: Testing.py -----")
    unittest.main()
