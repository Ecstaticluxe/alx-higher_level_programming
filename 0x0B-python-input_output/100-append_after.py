#!/usr/bin/python3

"""Inserts a line"""


def append_after(filename="", search_string="", new_string=""):

    """Inserts a line of text after each line
    containing a specific string in a file.
    Args:
    filename (str): The name of the file.
    search_string (str): The string being serached.
    new_string (str): The new string.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
