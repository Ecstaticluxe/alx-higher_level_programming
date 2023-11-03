#!/usr/bin/python3
# Import functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Define variables a and b
a = 10
b = 5

# Call the imported functions and print the results
result1 = add(a, b)
result2 = sub(a, b)
result3 = mul(a, b)
result4 = div(a, b)

# Print the results using only four print statements
print(f"{a} + {b} = {result1}")
print(f"{a} - {b} = {result2}")
print(f"{a} * {b} = {result3}")
print(f"{a} / {b} = {result4}")

