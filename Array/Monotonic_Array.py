# Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
#
# An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.
#
# Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.
#
# Note that empty arrays and arrays of one element are monotonic.
#
#
# Sample Input
# array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
#
# Sample Output
# true
import unittest


def isMonotonic(array: list) -> bool:
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
            break
        if array[i] > array[i - 1]:
            isNonIncreasing = False
            break
    return isNonDecreasing or isNonIncreasing


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)
