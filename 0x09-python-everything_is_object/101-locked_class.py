#!/usr/bin/python3

""" This module contains a class that avoids dynamically
created attributes """


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ init method"""
        pass
