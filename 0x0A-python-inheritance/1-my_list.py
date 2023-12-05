#!/usr/bin/python3
'''Inherits from list'''


class MyList(list):
    '''Inherits from list'''

def print_sorted(self):
    '''Prints the list in ascending order.'''
    sorted_list = sorted(self)
    print(sorted_list)

def _sort_list(self):
    '''Returns a sorted copy of the list'''

    sorted_list = self.copy()
    n = len(sorted_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j +1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                return (sorted_list)
