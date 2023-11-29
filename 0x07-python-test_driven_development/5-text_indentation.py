#!/usr/bin/python3
'''prints a text with two new lines after the caharactrs ., ? and :.'''


def text_indentation(text):
    '''
    Raises:
    TypeError: text must be a string.
    '''

    if not (isinstance(text, str):
    raise TypeError("text must be a string")

    current line = ""
    '''iterate through each character in the text'''

    for char in text:

    current_line += char
    '''check for the characters'''

    if char in ['.', '?', ':']:
    print(current_line.strip())
    print("\n" *2)

    '''
    Reset the current line'''

    current_line = ""

    if current_line:
    print(current_line.strip())
