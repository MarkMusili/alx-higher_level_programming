#!/usr/bin/python3
"""
This module defines a class
"""


class Student:
    """
    Stores data of a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Attributes:
            first_name (str): first name of student
            last_name (str) last name of student
            age (int) age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Convert data into json format
        """
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return data
