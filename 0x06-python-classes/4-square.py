#!/usr/bin/python3
"""This is a module that Creates a class called square"""


class Square:
    """
        This is a class representing a Square
        It has a private attribute size
    """
    def __init__(self, size=0):
        """
        Args:
            size(int): size of the square which is first initialized to 0
        Attributes:
            size(int) - size of the square
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
            This is a method that calulates the area of a square
            return size * size
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Property getter for size
        Return: int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a private instance of self that acts as a setter
        Return: int: value which is the new size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
