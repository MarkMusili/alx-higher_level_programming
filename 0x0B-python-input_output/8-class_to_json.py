#!/usr/bin/python3
"""
This module represents json data in a dictionary format
"""


def class_to_json(obj):
    """
    Args:
        obj (class): class instance
    Return:
        data(dict): deserilized data
    """
    data = {}

    for name in dir(obj):
        if not name.startswith("__"):
            value = getattr(obj, name)
            if isinstance(value, (list, dict, str, int, bool)):
                data[name] = value

    return data
