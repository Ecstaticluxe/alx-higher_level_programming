#!/usr/bin/python3
import sys

def add_args(argv):
    total = sum(int(arg) for arg in argv[1:])
    print(total)

if __name__ == "__main__":
    add_args(sys.argv)
