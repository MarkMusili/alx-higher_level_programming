#!usr/bin/python3
"""
This module defines a rectangle
"""
from base import Base


class Rectangle(Base):
    """
    This class inherits from Base class
    This class represents a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Attrubutes:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x-cordinates
            y (int): y-cordinates
            id (int): id associated with the instance
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if value <= 0:
            raise ValueError("Width  cannot be zero or less")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if value <= 0:
            raise ValueError("Height cannot be zero or less")
        self.__height = value

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        if value < 0:
            raise ValueError("x cannot be zero or less")
        self.__y = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        X setter
        """
        if value < 0:
            raise ValueError("x cannot be zero or less")
        self.__x = value
