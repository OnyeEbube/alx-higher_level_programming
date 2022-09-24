#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = my_list[:]
    if idx < 0 or idx > length:
        return(my_list)
    for s in range(length):
        if s == idx:
            new_list[s] = element
            return(new_list)
