#!/usr/bin/python3
# test_rectangle.py
"""Defines unittests for models/rectangle.py."""
import io
import sys
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
"""Unittests for testing instantiation of the Rectangle class."""
    def test_init(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 10)

    def test_width_setter_valid(self):
        rect = Rectangle(4, 5)
        rect.width = 7
        self.assertEqual(rect.width, 7)

    def test_width_setter_invalid_type(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            rect.width = "invalid"

    def test_width_setter_invalid_value(self):
        rect = Rectangle(4, 5)
        with self.assertRaises(ValueError):
            rect.width = -3

    # Similar tests for height, x, and y setters

    def test_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_display(self):
        with patch('builtins.print') as mock_print:
            rect = Rectangle(2, 3)
            rect.display()
            mock_print.assert_called_with("##\n##\n##")

    def test_str(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(str(rect), "[Rectangle] (10) 1/2 - 4/5")

    def test_update_with_args(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        rect.update(20, 6, 8, 3, 4)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_with_kwargs(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        rect.update(id=20, width=6, height=8, x=3, y=4)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        dictionary = rect.to_dictionary()
        expected_dict = {'id': 10, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(dictionary, expected_dict)

if __name__ == '__main__':
    unittest.main()

