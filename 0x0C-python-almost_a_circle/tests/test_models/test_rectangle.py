#!/usr/bin/python3
"""
This module performs unittest on our modules
"""
import unittest
import sys
from io import StringIO
from models.base import Base
from unittest.mock import patch
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    This module tests the base module
    """
    def setUp(self):
        self.stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_rectangle_constructor(self):
        """Test the rectangle class"""
        r1 = Rectangle(4, 5, 1, 1, 14)
        r2 = Rectangle(3, 6, 2, 2, 1)

        self.assertEqual(r1.id, 14)
        self.assertEqual(r2.id, 1)

    def test_rectangle_assingment(self):
        """Test the assignment operation on rectangle"""
        r1 = Rectangle(4, 5, 1, 1, 14)
        r2 = Rectangle(3, 6, 2, 2, 1)

        r1.width = 2
        r2.height = 5
        r1.x = 3
        r2.y = 4

        self.assertEqual(r1.width, 2)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r2.y, 4)

        with self.assertRaises(TypeError):
            r1.width = "4"
        with self.assertRaises(ValueError):
            r2.height = -3
        with self.assertRaises(ValueError):
            r2.x = -3

    def test_area(self):
        """Test the area method"""
        r1 = Rectangle(4, 5, 1, 1, 14)
        r2 = Rectangle(3, 6, 2, 2, 1)

        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 18)

    def test_display(self):
        """Test the display method"""
        r1 = Rectangle(2, 2)
        d1 = "##\n##\n"

        with patch('sys.stdout', new_callable=StringIO) as output:
            r1.display()
            output1 = output.getvalue()

        self.assertEqual(output1, d1)

    def test_display_with_spaces(self):
        """Test the display with spaces"""
        r1 = Rectangle(2, 2, 1, 1)
        d1 = '\n ##\n ##\n'

        with patch('sys.stdout', new_callable=StringIO) as output:
            r1.display()
            output1 = output.getvalue()

        self.assertEqual(output1, d1)

    def test_representation(self):
        """Test how the contents are represented"""
        r1 = Rectangle(5, 4, 1, 1, 12)
        self.assertEqual(str(r1), '[Rectangle] (12) 1/1 - 5/4')

    def test_update_with_args(self):
        """Test the update method positional arguments"""
        r1 = Rectangle(2, 4, 1, 1, 12)
        r1.update(24, 4, 8, 2, 2)
        self.assertEqual(str(r1), '[Rectangle] (24) 2/2 - 4/8')

    def test_update_with_kwargs(self):
        """Test the update method with key word argument"""
        r1 = Rectangle(2, 4, 1, 1, 12)
        r1.update(id=12, x=1, y=1, width=2, height=4)
        self.assertEqual(str(r1), '[Rectangle] (12) 1/1 - 2/4')

    def test_dictionary(self):
        """Test the representation in dictionary form"""
        r1 = Rectangle(2, 4, 1, 1, 12)
        output = r1.to_dictionary()
        dictionary = {'id': 12, 'width': 2, 'height': 4, 'x': 1, 'y': 1}
        self.assertEqual(output, dictionary)
