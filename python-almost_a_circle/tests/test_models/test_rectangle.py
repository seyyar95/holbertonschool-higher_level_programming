#!/usr/bin/python3

"""Test for Almost a Circle - Rectangle Class"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r = Rectangle(1, 2, 3, 4, 5)

    def test_attributes(self):
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)
        self.assertEqual(self.r.id, 5)
 
    def test_area(self):
        self.assertEqual(self.r.area(), 2)

    def test_to_dictionary(self):
        dictionary = {"width": 1, "height": 2, "x": 3, "y": 4, "id": 5}
        self.assertEqual(self.r.to_dictionary(), dictionary)

    def test_update(self):
        self.r.update(10, 20, 30, 40, 50)
        self.assertEqual(self.r.width, 20)
        self.assertEqual(self.r.height, 30)
        self.assertEqual(self.r.x, 40)
        self.assertEqual(self.r.y, 50)
        self.assertEqual(self.r.id, 10)
