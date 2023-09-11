#!/usr/bin/python3
"""
This module checks is an object is an instance \
of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: subclass to be checked
        a_class: base class to be checked
    Return:
        True: if the subclass is in base class
        False: if subclass is not it base class
    """
    return issubclass(type(obj), a_class)
