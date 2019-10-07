"""
Contains unit tests for Blackjack game
Author: Japjot Singh
"""
import unittest
from helper import Card

class TestStringMethods(unittest.TestCase):
    def test_rank_suit_vals(self):
        self.assertRaises(ValueError, Card, 14, "Spade")
        self.assertRaises(ValueError, Card, None, "Spade")
        self.assertRaises(ValueError, Card, "fourteen", "Spade")
        self.assertRaises(ValueError, Card, 14, "King")
        self.assertRaises(ValueError, Card, 6, None)
        self.assertRaises(ValueError, Card, None, 29)
        print("Card Init: PASSED")

if __name__ == "__main__":
    print("Running: Testing.py -----")
    unittest.main()
