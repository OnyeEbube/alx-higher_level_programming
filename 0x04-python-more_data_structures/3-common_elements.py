#!/usr/bin/python3
def common_elements(set_1, set_2):
    a = set(set_1)
    b = set(set_2)
    new_list = {x for x in a if x in b}
    return (new_list)
