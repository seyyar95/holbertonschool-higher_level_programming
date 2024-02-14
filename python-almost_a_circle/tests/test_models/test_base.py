#!/usr/bin/python3
""""Tests for Python - Almost a circle"""


import unittest
from models.base import Base

class BaseTest(unittest.TestCase):
    def test_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base(None)
        self.assertEqual(base2.id, 2)

        base3 = Base(89)
        self.assertEqual(base3.id, 3)


if __name__ == "__main__":
    unittest.main()

