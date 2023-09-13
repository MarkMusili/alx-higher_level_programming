#!/usr/bin/python3
"""
This module checks wether an object is inherited
from a specific class
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: subclass to be checked
        a_class: base class to be checked
    Return:
        True: if the subclass is in base class
        False: if subclass is not it base class
    """
    return isinstance(obj, a_class)
