#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    number1 = number % 10
    return(number1)
