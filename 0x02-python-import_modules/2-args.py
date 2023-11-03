#!/usr/bin/python3
import sys

args = sys.argv[1:]

num_args = len(args)

if num_args == 0:
    print("0 arguments.")
    print(".\n")
else:
    print("{} argument{}:".format(num_args, "" if num_args == 1 else "s"))
    for i, arg in enumerate(args):
        print("{}: {}".format(i+1, arg))
