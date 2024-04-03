# Bubble Sort
#
# Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort algorithm to sort the
# array.
#
# If you're unfamiliar with Bubble Sort, we recommend watching the Conceptual Overview section of this question's video explanation before
# starting to code.
#
# Sample Input
# array = [8, 5, 2, 9, 5, 6, 3]
#
# Sample Output
# [2, 3, 5, 5, 6, 8, 9]


import unittest


def bubbleSort(array: list) -> list:
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for idx in range(len(array) - 1 - counter):
            if array[idx] > array[idx + 1]:
                swap(idx, array)
                is_sorted = False
        counter += 1
    return array


def swap(idx: int, array: list) -> None:
    array[idx], array[idx + 1] = array[idx + 1], array[idx]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(bubbleSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
