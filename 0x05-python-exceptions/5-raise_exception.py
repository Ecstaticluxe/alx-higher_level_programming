#!/usr/bin/python3

def raise_exception():
    try:

        result = "string" + 5
    except TypeError as e:

        print("Type error:", e)
