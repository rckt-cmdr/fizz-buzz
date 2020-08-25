#!/usr/bin/python3

# File: test_fizz-buzz.py
# Author: Jonathan Belden
# Description: Test module for the Fizz_Buzz Coding Challenge
# Reference: https://edabit.com/challenge/WXqH9qvvGkmx4dMvp


import pytest
from src import fizz_buzz


@pytest.fixture
def inputValues():
    return [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25]

def test_1_OutputEqualsFizz(inputValues):
    # if input is a multiple of 3, output is "Fizz"
    
    for value in inputValues:
        result = fizz_buzz.evaluate(value)
        assert result is type(str) , "Result should be a string"
        assert result == "Fizz",  "Result should be 'Fuzz'"

def test_2_OutputEqualsBuzz():
    pass
    # if input is a multiple of 5, output is "Buzz"

def test_3_OutputEqualsFizzBuzz():
    pass
    # if input is multiple of 3 or 5, output is "FizzBuzz"

def test_4_OutputEqualsInput():
    pass
    # if input is NOT a multiple of 3 or 5, output is same as input