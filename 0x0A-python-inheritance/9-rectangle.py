#!/usr/bin/python3
"""
This module impliments a subclass Rectangle
that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is a subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantation of Rectangle
        Attributes:
            width (int): width of rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        User frienly representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
