#!/usr/bin/python3
"""
This module defines a function:
that checks whether an object  is in a class
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object to be checked
        a_class: class to be checked
    Return:
        True: if the object is in class
        False: if object is not it class
    """
    return isinstance(obj, a_class)
