#!/usr/bin/python3
"""
This module performs unittest on our modules
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    This module tests the base module
    """

    def test_base(self):
        """Test the basic constructor"""
        b1 = Base()
        b2 = Base()
        b3 = Base(14)
        b4 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 14)
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test the to_json_string method"""
        r1 = Rectangle(2, 4, 1, 1, 12)
        dictionary_1 = r1.to_dictionary()
        json_string_1 = r1.to_json_string([dictionary_1])
        json_string_2 = r1.to_json_string(None)
        output_1 = '[{"id": 12, "width": 2, "height": 4, "x": 1, "y": 1}]'
        output_2 = "[]"
        self.assertEqual(json_string_1, output_1)
        self.assertEqual(json_string_2, output_2)

    def test_save_to_file(self):
        """Test the save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8, 12)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            compare = file.read()

        self.assertTrue(compare)

    def test_from_json_string(self):
        """Test from_json_string"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
            ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        expected = [
            {'height': 4, 'width': 10, 'id': 89},
            {'height': 7, 'width': 1, 'id': 7}
        ]
        empty = '[]'
        self.assertEqual(list_output, expected)
    
    def from_json_string(self):
        """Test an empty string"""
        self.assertEqual('[]', Base.from_json_string(None))
        self.assertEqual([], Base.from_json_string(empty))

    def test_create(self):
        """Test create method"""
        r1 = Rectangle(4, 8, 1, 1, 12)
        dictionary = r1.to_dictionary()
        r2 = r1.create(**dictionary)
        o1 = dir(r1)
        o2 = dir(r2)
        self.assertEqual(o1, o2)

    def test_load_from_file(self):
        """Test the load_from_file method"""
        r1 = Rectangle(4, 8, 1, 1, 12)
        r2 = Rectangle(8, 16, 2, 2, 24)
        Rectangle.save_to_file([r1, r2])

        output = Rectangle.load_from_file()
        loaded_dict = [item.to_dictionary() for item in output]
        with open('Rectangle.json') as file:
            list_of_instances = json.load(file)
        self.assertEqual(loaded_dict, list_of_instances)
