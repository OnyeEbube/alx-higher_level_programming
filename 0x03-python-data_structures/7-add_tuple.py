#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length1 = len(tuple_a)
    length2 = len(tuple_b)
    if length1 == 0:
        tuple_a = (0, 0)
    if length2 == 0:
        tuple_b = (0, 0)
    if length1 == 1:
        tuple_a = (tuple_a[0], 0)
    if length2 == 1:
        tuple_b = (tuple_b[0], 0)
    if length1 > 2:
        tuple_a = (tuple_a[:2])
    if length2 > 2:
        tuple_b = (tuple_b[:2])
    sum1 = tuple_a[0] + tuple_b[0]
    sum2 = tuple_a[1] + tuple_b[1]
    new_tuple = (sum1, sum2)
    return(new_tuple)
