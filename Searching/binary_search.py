# Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm
# to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.
#
# If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of this question's video explanation
# before starting to code.
#
# Sample Input
# array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
# target = 33
#
# Sample Output
# 3

import unittest


def binarySearch(array: list, target: int) -> int:
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array: list, target: int, left: int, right: int) -> int:
    while left <= right:
        mid = (left + right) // 2
        potential_match = array[mid]
        if target == potential_match:
            return mid
        elif target > potential_match:
            left = mid + 1
        else:
            right = mid - 1
    return -1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)

    def test_case_2(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 1), 1)

    def test_case_3(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 55, 61, 71, 72, 73], 55), 5)
