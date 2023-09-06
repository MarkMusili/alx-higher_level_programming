#!/usr/bin/python3
"""This is class that represents a rectangle"""


class Rectangle:
    """
    This class has the first instance as:
    Arguments:
        width (int): width of a rectangle
        height (int): height of a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is a property getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        This is a property setter for width
        Args:
            value(int): new value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This is a property getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is a property setter for height
        Args:
            value(int): new value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
