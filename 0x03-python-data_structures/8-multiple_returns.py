#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    firstChr = sentence[0]
    if length == 0:
        new_tuple = (length, None)
    else:
        new_tuple = (length, firstChr)
    return(new_tuple)
