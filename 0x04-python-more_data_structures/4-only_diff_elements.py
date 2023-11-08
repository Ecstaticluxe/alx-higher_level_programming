#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    only_diff_set = set(set_1.symmetric_difference(set_2))
    return only_diff_set

# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
result = only_diff_elements(set1, set2)
print(result)  # Output will be {1, 2, 6, 7}
