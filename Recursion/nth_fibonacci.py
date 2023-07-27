# The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth number is the sum
# of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number.
#
# Important note: the Fibonacci sequence is often defined with its first two numbers as F0 = 0 and F1 = 1. For the purpose of this question,
# the first Fibonacci number is F0; therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc..
#
# Sample Input #1
# n = 2
#
# Sample Output #1
# 1 // 0, 1
#
# Sample Input #2
# n = 6
#
# Sample Output #2
# 5 // 0, 1, 1, 2, 3, 5

import unittest

chache = {1: 0, 2: 1}


def getNthFib(n):
    if n in chache:
        return chache[n]
    else:
        nth_fib = getNthFib_iter(n - 1) + getNthFib_iter(n - 2)
        chache[n] = nth_fib
        return nth_fib


def getNthFib_iter(n):
    fib = [0, 1]
    curr = 3
    while curr <= n:
        next_fib = fib[0] + fib[1]
        fib[0] = fib[1]
        fib[1] = next_fib
        curr += 1

    return fib[1] if n > 1 else fib[0]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(getNthFib_iter(15), 377)

    def test_case_2(self):
        self.assertEqual(getNthFib_iter(15), 377)
