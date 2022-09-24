#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = my_list
    length = len(new_list)
    if idx < 0 or idx > length:
        return(my_list)
    for l in range(length):
        if l == idx:
            new_list[l] = element
            return(new_list)
