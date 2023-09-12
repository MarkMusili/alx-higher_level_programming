#!/usr/bin/python3
"""
This module encodes an object to JSON format
"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj (string): object to be converted
    Return:
        JSON representation of the object
    """
    string = json.dumps(my_obj)
    return string
