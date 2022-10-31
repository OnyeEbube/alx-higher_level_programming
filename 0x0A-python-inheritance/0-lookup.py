#!/usr/bin/python3

"""creating a function. """


def lookup(obj):
    """ This is a function that returns the list of available
    attributes and methods of an object.

    Args:
        obj: instance of the class
    """

    return dir(obj)
