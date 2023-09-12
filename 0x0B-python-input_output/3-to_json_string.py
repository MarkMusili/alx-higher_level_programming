#!/usr/bin/python3
import json
"""
This module encodes an object to JSON format
"""


def to_json_string(my_obj):
    """
    Args:
        my_obj (string): object to be converted
    Return:
        JSON representation of the object
    """
    return json.dumps(my_obj)
