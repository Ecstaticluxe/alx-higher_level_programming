#!/usr/bin/python3
'''Define class name'''


def say_my_name(first_name, last_name=""):

    '''Represent a name
    Args:
    first_name (str): The first name.
    last_name (str): The last name.
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name mustbe a string")

    print(f"My name is {first_name} {last_name}")

