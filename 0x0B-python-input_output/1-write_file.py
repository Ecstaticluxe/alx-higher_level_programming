#!/usr/bin/python3

"""A text file UTF8"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    and returns the number of characters written.
    Args:
    filename (str):The name of the file.
    text (str): the text of teh file.
    Returns;
    the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))