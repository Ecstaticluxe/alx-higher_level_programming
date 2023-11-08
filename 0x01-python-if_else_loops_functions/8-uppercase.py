#!/usr/bin/python3

def uppercase(input_str):
    result = ""

    for char in input_str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char

    return result

input_string = "Best School 98 Battery street"
uppercase_string = uppercase(input_string)
print(uppercase_string)
