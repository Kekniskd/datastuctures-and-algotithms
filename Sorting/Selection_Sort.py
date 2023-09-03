# Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort algorithm to sort the
# array.
#
# If you're unfamiliar with Selection Sort, we recommend watching the Conceptual Overview section of this question's video explanation before
# starting to code.
#
# Sample Input
# array = [8, 5, 2, 9, 5, 6, 3]
#
# Sample Output
# [2, 3, 5, 5, 6, 8, 9]


import unittest


def selectionSort(array: list) -> list:
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array


def swap(i: int, j: int, array: list) -> None:
    array[i], array[j] = array[j], array[i]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(selectionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
