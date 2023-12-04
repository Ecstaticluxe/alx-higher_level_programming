#!/usr/bin/python3
'''Contain "is_kind_of_class" function'''


def is_kind_of_class(obj, a_class):
    ''' returns True if the object is an instance or inherited from,
    the specified class ; otherwise False.'''

    return (isinstance(obj, a_class))
