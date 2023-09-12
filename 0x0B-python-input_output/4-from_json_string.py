#!/usr/bin/python3
"""
This module decodes an object to JSON format
"""
import json


def from_json_string(my_obj):
    """
    Args:
        my_obj (string): object to be converted
    Return:
        Python representation of the object
    """
    string = json.loads(my_obj)
    return string
