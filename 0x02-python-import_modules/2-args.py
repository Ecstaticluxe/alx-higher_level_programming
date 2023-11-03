#!/usr/bin/python3
import sys

def print_arguments(argv):
    num_arguments = len(argv)
    if num_arguments == 0:
        print("Number of argument(s) : .")
    else:
        print(f"Number of argument(s): {num_arguments}{'s' if num_arguments > 1 else ''} :")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments(sys.argv[1:])
