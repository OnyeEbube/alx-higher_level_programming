#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return(my_list)
    for s in my_list[:]:
        if s == my_list[idx]:
            my_list[idx] = element
            return(my_list)
