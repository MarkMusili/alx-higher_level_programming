#!/usr/bin/python3
"""
This module defines a square
"""
from models.rectangle import Rectangle


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

    def update(self, *args, **kwargs):
        """
        Updates the values for square
        Args:
            args: Take positional arguments
            kwargs: Take Key word arguments
        """
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """
        Represent as a dictionary
        Return:
            my_dict - dictionary
        """
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['size'] = self.size
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
