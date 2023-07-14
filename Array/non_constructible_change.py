# Given an array of positive integers representing the values of coins in your possession, write a function that
# returns the minimum amount of change (the minimum sum of money) that you cannot create. The given coins can have
# any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).
#
# For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4. If you're
# given no coins, the minimum amount of change that you can't create is 1.
#
# Sample Input
# coins = [5, 7, 1, 1, 2, 3, 22]
#
# Sample Output
# 20

import unittest


def nonConstructibleChange(coins: list) -> int:
    coins.sort()

    curr_change = 0
    for coin in coins:
        if coin > curr_change + 1:
            return curr_change + 1
        curr_change += coin
    return curr_change + 1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        actual = nonConstructibleChange(input)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    test_case_1_obj = TestProgram()
    test_case_1_obj.test_case_1()
