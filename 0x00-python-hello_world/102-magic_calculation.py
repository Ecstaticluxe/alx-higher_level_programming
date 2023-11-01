#!/usr/bin/python3
def magic_calculation(a, b):

    result = 98
    result = result ** a
    result = result + b
    return result

a = 2
b = 3
expected_result = 98 ** a + b
result = magic_calculation(a, b)
print(result)
