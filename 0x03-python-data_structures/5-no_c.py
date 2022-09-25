#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    x = 0
    newString = my_string[:]
    for s in range(length):
        if (my_string[s] == 'c' or my_string[s] == 'C'):
            newString = newString[:(s - x)] + my_string[(s + 1):]
            x += 1
    return(newString)
