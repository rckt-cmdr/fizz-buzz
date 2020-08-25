#!/usr/bin/python3

# File: test_fizz-buzz.py
# Author: Jonathan Belden
# Description: Test module for the Fizz_Buzz Coding Challenge
# Reference: https://edabit.com/challenge/WXqH9qvvGkmx4dMvp


import unittest
from src import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.multiplesOfThree = [3, 6, 9, 12]  # specific values that are *only* multiples of 3
        self.multiplesOfFive = [5, 10, 20, 25]  # specific values that are *only* multiples of 5
        self.multiplesOfThreeAndFive = [15, 30, 45, 60]  # specific values that are *only* multiples of both 3 *and* 5

    def test_1_OutputEqualsFizz(self):
        # if input is a multiple of 3, output is "Fizz"
        
        for value in self.multiplesOfThree:
            result = fizz_buzz.evaluate(value)
            self.assertIsInstance(result, str)
            self.assertEquals(result, "Fizz")

    def test_2_OutputEqualsBuzz(self):
        pass
        # if input is a multiple of 5, output is "Buzz"

    def test_3_OutputEqualsFizzBuzz(self):
        pass
        # if input is multiple of 3 and 5, output is "FizzBuzz"

    def test_4_OutputEqualsInput(self):
        pass
        # if input is NOT a multiple of 3 or 5, output is same as input


if __name__ == "__main__":
    unittest.main()