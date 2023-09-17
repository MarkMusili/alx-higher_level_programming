#!/usr/bin/python3
"""
This module defines a square
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    This class Represents a square
    that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        Attributes:
            size (int): size of the square
            x (int): spaces on the x co-ordinate
            y (int): spaces on the y co-ordinate
            id (int): id associated with the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Represent the square in user friendly manner
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """The getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = value
