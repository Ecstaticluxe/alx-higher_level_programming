#!/usr/bin/python3
'''An inherited class'''


def inherits_from(obj, a_class):
    '''Returns True if the object is an instance of a class that inherited
    from the specified class; otherwise False.'''

    obj_class = type(obj)

    if obj_class == a_class:
        return (True)
    for base_class in obj_class.__bases__:
        if inherits_from(base_class(), a_class):
            return (True)
        return (False)
