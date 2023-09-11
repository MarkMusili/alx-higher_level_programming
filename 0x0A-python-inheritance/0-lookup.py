#!/usr/bin/python3
"""
This is a module that performs a look-up on a class
"""


def lookup(obj):
    """
    Arg:
        obj: class to be perfomed the look up
    Return:
        a list of the available attributes and methods
    """
    my_list = dir(obj)
    return my_list
