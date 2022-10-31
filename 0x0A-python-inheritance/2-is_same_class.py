#!/usr/bin/python3

"""creating a function."""


def is_same_class(obj, a_class):
    """This function returns True if the object is exactly an instance
    of the specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
