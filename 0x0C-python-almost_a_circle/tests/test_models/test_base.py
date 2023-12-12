#!/usr/bin/python3
"""Defines unittests for base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
"""Unittests for testing instantiation of the Base class."""

    def test_init_with_id(self):
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)

    def test_init_without_id(self):
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        result = Base.to_json_string([{'id': 1, 'name': 'object'}])
        self.assertEqual(result, '[{"id": 1, "name": "object"}]')

    def test_save_to_file(self):
        with patch('builtins.open', create=True) as mock_open:
            base_instance = Base()
            Base.save_to_file([base_instance])
            mock_open.assert_called_with('Base.json', 'w')
            mock_open().write.assert_called_with('[{"id": 1}]')

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string('')
        self.assertEqual(result, [])

    def test_from_json_string_non_empty_string(self):
        result = Base.from_json_string('[{"id": 1, "name": "object"}]')
        self.assertEqual(result, [{'id': 1, 'name': 'object'}])

    def test_create_rectangle(self):
        with patch('models.rectangle.Rectangle') as mock_rect:
            result = Base.create(id=1, width=2, height=3)
            mock_rect.assert_called_with(id=1, width=1, height=1)
            self.assertEqual(result, mock_rect())

    def test_create_square(self):
        with patch('models.square.Square') as mock_square:
            result = Base.create(id=1, size=2)
            mock_square.assert_called_with(id=1, size=1)
            self.assertEqual(result, mock_square())

    def test_load_from_file(self):
        with patch('builtins.open', create=True) as mock_open:
            mock_open().read.return_value = '[{"id": 1}]'
            with patch('models.base.Base.create') as mock_create:
                result = Base.load_from_file()
                mock_create.assert_called_with(id=1)
                self.assertEqual(result, [mock_create()])

if __name__ == '__main__':
    unittest.main()

