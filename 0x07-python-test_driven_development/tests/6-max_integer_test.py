#!/usr/bin/python3


import unittest
from your_module_name import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_integers(self):
        result = max_integer([1, 3, 2, 8, 6])
        self.assertEqual(result, 8)

    def test_negative_integers(self):
        result = max_integer([-1, -5, -2, -8, -6])
        self.assertEqual(result, -1)

    def test_mixed_integers(self):
        result = max_integer([-1, 5, 2, -8, 6])
        self.assertEqual(result, 6)

    def test_duplicate_integers(self):
        result = max_integer([3, 3, 3])
        self.assertEqual(result, 3)

    def test_floats(self):
        result = max_integer([1.5, 2.5, 1.2, 3.8])
        self.assertEqual(result, 3.8)

if __name__ == '__main__':
    unittest.main()
