#!/usr/bin/python3
"""
This module defines a rectangle
"""
from models.base import Base


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
            x (int): x-spaces
            y (int): y-spaces
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """Calculates the area"""
        return self.width * self.height

    def display(self):
        """Displays the rectangle"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        """Print a user friendly representation"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates values of Rectangle"""
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)
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
        my_dict['width'] = self.width
        my_dict['height'] = self.height
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
