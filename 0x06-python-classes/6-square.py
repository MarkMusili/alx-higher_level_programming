#!/usr/bin/python3
"""This is a module that Creates a class called square"""


class Square:
    """
        This is a class representing a Square
        It has a private attribute size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size(int): size of the square which is first initialized to 0
            position (tuple): use for indexing the square
        Attributes:
            size(int) - size of the square
        """
        self.__size = size
        self.__position = position
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

    def my_print(self):
        """
        This is a public instance where it prints '#' to form the square
        Returns: '#'chars that form a square
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """This is a getter for the position instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """This is the setter for the position instance"""
        if type(value) is not tuple or len(tuple) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
