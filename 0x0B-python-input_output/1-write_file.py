#!/usr/bin/python3

""" Creating a function. """


def write_file(filename="", text=""):
    """ This function writes a string to a text file (UTF*) and
    returns the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as x:
        return x.write(text)
