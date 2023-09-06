#!/usr/bin/python3
"""
This module defines a function that adds two integers
"""
def add_integer(a, b=98):
    """
    args:
        a (int): first integer
        b (int): second integer
    Return:
        sum of the two integers
    """
    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    result = a + b

    return result
