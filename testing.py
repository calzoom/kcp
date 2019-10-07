"""
Contains unit tests for Blackjack game
Author: Japjot Singh
"""
import unittest
from helper import Card

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

if __name__ == "__main__":
    print("Running: Testing.py -----")
    unittest.main()
