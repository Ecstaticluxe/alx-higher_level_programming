#!/usr/bin/python3
def print_reversed_list_integer(my_list=None):
    if my_list is None:
        my_list = []  # Create a new list if my_list is not provided
    for i in my_list[::-1]:
        print("{!r}".format(i))
