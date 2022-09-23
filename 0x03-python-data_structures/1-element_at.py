#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx > length or idx < 0:
        return(None)
    for l in range(length):
        if l == idx:
            return(my_list[idx])
