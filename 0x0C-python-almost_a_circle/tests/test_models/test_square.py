#!/usr/bin/python3
#test_square.py
"""Defines unittests for models/square.py."""

import io
import sys
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
"""Unittests for testing instantiation of the Square class."""

    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_initialization(self):
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.height, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

    def test_size_property(self):
        self.square.size = 8
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.width, 8)
        self.assertEqual(self.square.height, 8)

    def test_update_method_with_args(self):
        self.square.update(10, 7, 8, 4)
        self.assertEqual(self.square.id, 10)
        self.assertEqual(self.square.size, 7)
        self.assertEqual(self.square.x, 8)
        self.assertEqual(self.square.y, 4)

    def test_update_method_with_kwargs(self):
        self.square.update(id=15, size=3, x=1, y=9)
        self.assertEqual(self.square.id, 15)
        self.assertEqual(self.square.size, 3)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 9)

    def test_to_dictionary_method(self):
        square_dict = self.square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

    def test_str_representation(self):
        str_repr = str(self.square)
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str_repr, expected_str)

if __name__ == '__main__':
    unittest.main()
