#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    list_result = []
    for s in range(length):
        if my_list[s] % 2 == 0:
            list_result.append(True)
        else:
            list_result.append(False)
    return (list_result)
