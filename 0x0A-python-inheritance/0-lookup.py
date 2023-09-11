#!/usr/bin/python3
"""
This module performs a lookup on a class
"""


def lookup(obj):
    """
    Arg:
        obj: class to be performed the lookup
    Return:
        list of all the attributes, methods of the class
    """
    my_list = dir(obj)
    return my_list
