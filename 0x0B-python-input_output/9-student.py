#!/usr/bin/python3

"""A class student"""


class Student:
    """A class that defines a student"""


def __init__(self, first_name, last_name, age):
    """Initialise a new Student.
    Args:
    first_name (str): the first name.
    last name (str): the last name.
    age (int): the age of the student.
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        __import__("8-class_to_json_file")
        return self
