#!/usr/bin/python3
"""
This module performs unittest on our modules
"""
import unittest
import sys
from io import StringIO
from models.base import Base
from unittest.mock import patch
from models.square import Square


class TestBase(unittest.TestCase):
    """
    This module tests the base module
    """
    def setUp(self):
        self.stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_square_constructor(self):
        """Test the square class"""
        s1 = Square(4, 1, 1, 14)
        s2 = Square(3, 2, 2, 1)

        self.assertEqual(s1.id, 14)
        self.assertEqual(s2.id, 1)

    def test_square_assingment(self):
        """Test the assignment operation on square"""
        s1 = Square(4, 1, 1, 14)
        s2 = Square(6, 2, 2, 1)

        s1.size = 2
        s2.size = 2
        s1.x = 3
        s2.y = 4

        self.assertEqual(s1.size, 2)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s2.y, 4)

        with self.assertRaises(TypeError):
            s1.size = "4"
        with self.assertRaises(ValueError):
            s2.size = -3
        with self.assertRaises(ValueError):
            s2.x = -3

    def test_area(self):
        """Test the area method"""
        s1 = Square(4, 1, 1, 14)
        s2 = Square(6, 2, 2, 1)

        self.assertEqual(s1.area(), 16)
        self.assertEqual(s2.area(), 36)

    def test_display(self):
        """Test the display method"""
        s1 = Square(2, 2)
        d1 = "  ##\n  ##\n"

        with patch('sys.stdout', new_callable=StringIO) as output:
            s1.display()
            output1 = output.getvalue()

        self.assertEqual(output1, d1)

    def test_display_with_spaces(self):
        """Test the display with spaces"""
        s1 = Square(2, 1, 2)
        d1 = '\n\n ##\n ##\n'

        with patch('sys.stdout', new_callable=StringIO) as output:
            s1.display()
            output1 = output.getvalue()

        self.assertEqual(output1, d1)

    def test_representation(self):
        """Test how the contents are represented"""
        s1 = Square(4, 1, 1, 12)
        self.assertEqual(str(s1), '[Square] (12) 1/1 - 4')

    def test_update_with_args(self):
        """Test the update method positional arguments"""
        s1 = Square(4, 1, 1, 12)
        s1.update(24, 8, 2, 2)
        self.assertEqual(str(s1), '[Square] (24) 2/2 - 8')
    
    def test_update_with_kwargs(self):
        """Test the update method with key word argument"""
        s1 = Square(4, 1, 1, 12)
        s1.update(id=12, x=1, y=1, size=4)
        self.assertEqual(str(s1), '[Square] (12) 1/1 - 4')

    def test_dictionary(self):
        """Test the representation in dictionary form"""
        s1 = Square(2, 1, 1, 12)
        output = s1.to_dictionary()
        self.assertEqual(output, {'id': 12, 'size': 2, 'x': 1, 'y': 1})
