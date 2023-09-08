#!/usr/bin/python3
"""
This moduleprints:
    A sqaure with the character '#'
Without importing any module
"""


def print_square(size):
    """
    Arg:
        size (int): size length of the square
    Return:
        Representation of the square using the character '#'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be and integer")

    for _ in range(size):
        print('#' * size)
