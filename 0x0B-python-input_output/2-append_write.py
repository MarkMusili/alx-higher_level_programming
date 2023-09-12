#!/usr/bin/python3
"""
This module appends text to a text-file
"""


def append_write(filename="", text=""):
    """
    Args:
        filename (str): file path
        text (str): text to be appended
    Return:
        count(int): number of characters added
    """
    with open(filename, 'a') as f:
        count = f.write(text)
        return count
