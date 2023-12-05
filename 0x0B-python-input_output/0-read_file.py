#!/usr/bin/python3
'''Text file of UTF8'''


def read_file(filename=""):
    '''a function that reads a text file (UTF8) and prints it to stdout.'''

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
            '''raises exception'''
    except Exception as e:
        print(f"An error occurred: {e}")

