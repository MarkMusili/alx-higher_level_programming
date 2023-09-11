#!/usr/bin/python3
"""
This module defines a base class and a subclass:
    List(base-class), Mylist(sub-class)
"""


class MyList(list):
    """
    This class has a public instance method
    """
    def print_sorted(self):
        """
        This method prints a list in a sorted manner
        """
        print(sorted(self))
