#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    max_int = my_list[0]
    for s in range(1, len(my_list)):
        if my_list[s] > max_int:
            max_int = my_list[s]
    return (max_int)
