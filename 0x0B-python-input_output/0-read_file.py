#!/usr/bin/python3

"""Creating a function. """


def read_file(filename=""):
    """ This function reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r', encoding="utf-8") as x:
        read_data = x.read()
        print(read_data, end='')
