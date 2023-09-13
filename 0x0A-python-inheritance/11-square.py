#!/usr/bin/python3
"""
This class inherits from rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class impliments a square
    """
    def __init__(self, size):
        """
        Attributes:
            size(int): size of the square
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Represent the square
        """
        return f"[Square] {self.__size}/{self.__size}"
