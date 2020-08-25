#!/usr/bin/python3

# File: fizz_buzz.py
# Author: Jonathan Belden
# Description: Fizz-Buzz Coding Challenge
# Reference: https://edabit.com/challenge/WXqH9qvvGkmx4dMvp


def evaluate(inputValue):
    result = None

    if inputValue % 3 == 0 and inputValue % 5 == 0:
        result = "FizzBuzz"
    elif inputValue % 3 == 0:
        result = "Fizz"
    elif inputValue % 5 == 0:
        result = "Buzz"
    else:
        result = str(inputValue)

    return result