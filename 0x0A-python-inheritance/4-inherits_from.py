#!/usr/bin/python3
'''An inherited class'''


def inherits_from(obj, a_class):
    '''Returns true if the object is a subclass of a class, else, false.'''
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
