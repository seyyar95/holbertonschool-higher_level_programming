#!/usr/bin/python3
""""Tests for Python - Almost a circle"""


import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    def test_id_checker(self):
        # None case
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b1 = Base(None)
        self.assertEqual(b1.id, 2)

        # Positive integer case
        b2 = Base(3)
        self.assertEqual(b2.id, 3)

        b2 = Base(4)
        self.assertEqual(b2.id, 4)

        # Negative integer case
        b3 = Base(-5)
        self.assertEqual(b3.id, -5)

        b3 = Base(-6)
        self.assertEqual(b3.id, -6)

        # String case
        b4 = Base("Saul Goodman was here.")
        self.assertEqual(b4.id, "Saul Goodman was here.")

        b4 = Base("If you don't like Kanye, I don't like you.")
        self.assertEqual(b4.id, "If you don't like Kanye, I don't like you.")


if __name__ == "__main__":
    unittest.main()
