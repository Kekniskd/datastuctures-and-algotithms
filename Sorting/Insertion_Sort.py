# Write a function that takes in an array of integers and returns a sorted version of that array. Use the Insertion Sort algorithm to sort the
# array.

# If you're unfamiliar with Insertion Sort, we recommend watching the Conceptual Overview section of this question's video explanation before
# starting to code.

# Sample Input
# array = [8, 5, 2, 9, 5, 6, 3]

# Sample Output
# [2, 3, 5, 5, 6, 8, 9]


import unittest


def insertionSort(array: list) -> list:
    for idx in range(1, len(array)):
        curr_idx = idx
        while curr_idx > 0 and array[curr_idx] < array[curr_idx - 1]:
            swap(curr_idx, array)
            curr_idx -= 1
    return array


def swap(idx: int, array: list) -> None:
    array[idx], array[idx - 1] = array[idx - 1], array[idx]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(insertionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
