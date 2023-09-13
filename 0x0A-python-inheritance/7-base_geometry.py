#!/usr/bin/python3
"""
This module defines a class for doing geometry
"""


class BaseGeometry:
    """
    This class has a public instnace method for calculating/
    area
    """
    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        Args:
            name(str): A string
            value (int): Integer value to be validates
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
