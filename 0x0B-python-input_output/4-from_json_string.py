#!/usr/bin/python3

""" Creating a function. """
import json


def from_json_string(my_str):
    """ This function returns the object (Python data structure) represented
    by a JSONstring"""
    return json.loads(my_str)
