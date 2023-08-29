#!/usr/bin/python3
"""This is a module that Creates a class called square"""


class Square:
    """
        This is a class representing a Square
        It has a private attribute size
    """
    def __init__(self, size):
        """
        Args:
            size(int): size of the square
        Attributes:
            size(int) - size of the square
        """
        self._size = size
