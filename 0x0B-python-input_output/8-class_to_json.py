#!/usr/bin/python3

""" Creating a function. """


def class_to_json(obj):
    """ This function returns the dictionary description with simple data
    structure for JSON serialization of an object.
    """
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
