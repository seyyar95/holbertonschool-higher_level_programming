#!/usr/bin/python3
""""Tests for Python - Almost a circle"""


import unittest
from models.base import Base

class BaseTest(unittest.TestCase):
    def test_id(self):
        # None case

        base1 = Base()
        self.assertEqual(base1.id, 1)

        base1 = Base(None)
        self.assertEqual(base1.id, 2)

        # positive int case
        base1 = Base(10)
        self.assertEqual(base1.id, 10)

        base1 = Base(100)
        self.assertEqual(base1.id, 100)

        # negative int case
        base1 = Base(-1)
        self.assertEqual(base1.id, -1)

        base1 = Base(-25)
        self.assertEqual(base1.id, -25)


if __name__ == "__main__":
    unittest.main()

