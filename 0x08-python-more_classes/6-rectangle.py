#!/usr/bin/python3
"""This is class that represents a rectangle"""


class Rectangle:
    """
    This class has the first instance as:
    Arguments:
        width (int): width of a rectangle
        height (int): height of a rectangie
    Attribute:
        number_of_instances - number of rectangles
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This is a public instance that calculates the area"""
        return self.__height * self.__width

    def perimeter(self):
        """This is a public instance that calculates perimeter"""
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """This is a representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for _ in range(self.__height):
            rectangle += '#' * self.__width + '\n'
        return rectangle.rstrip()

    def __repr__(self):
        """This is a formal representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """This method will detect whether an istance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
