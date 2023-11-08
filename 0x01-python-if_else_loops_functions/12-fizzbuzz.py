#!/usr/bin/python3

def fizzbuzz():
    for c in range(1, 100):
        if c % 3 == 0 and c % 5 == 0:
            print("FizzBuzz")
        elif c % 3 == 0:
            print("Fizz")
        elif c % 5 == 0:
            print("Buzz")
        else:
            print(c)

fizzbuzz()
