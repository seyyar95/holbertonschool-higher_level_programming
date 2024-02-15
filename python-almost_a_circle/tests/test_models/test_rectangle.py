#!/usr/bin/python3

"""Test for Almost a Circle - Rectangle Class"""


import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r = Rectangle(1, 2, 3, 4, 5)

    def test_attributes(self):
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)
        self.assertEqual(self.r.id, 5)

    def test_attributes_2(self):
        # without x y
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        # without y
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

        # all attributes
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

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

    def test_typeErrors(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle("5", 7)
        with self.assertRaises(TypeError):
            Rectangle(5, "7")
        with self.assertRaises(TypeError):
            Rectangle(5, 7, "4")
        with self.assertRaises(TypeError):
            Rectangle(5, 7, 4, "3")

    def test_valueErrors(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_str(self):
        self.assertEqual(str(self.r), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        # without x and y exists
        r = Rectangle(3, 3, 0, 0)
        output = "###\n###\n###\n"
        with patch("sys.stdout", new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), output)

    def test_display_2(self):
        output = "\n\n\n\n   #\n   #\n"
        with patch("sys.stdout", new=StringIO()) as out:
            self.r.display()
            self.assertEqual(out.getvalue(), output)
