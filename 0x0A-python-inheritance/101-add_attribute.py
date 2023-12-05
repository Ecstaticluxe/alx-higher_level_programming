#!/usr/bin/python3
'''An attribute to an objeect'''


def add_attribute(obj, attribute_name, attribute_value):
    """Adds a new attribute to an object if possible."""

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[attribute_name] = attribute_value
