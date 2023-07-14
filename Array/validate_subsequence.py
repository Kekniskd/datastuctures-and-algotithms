# Given two non-empty arrays of integers, our goal is to write a function that establishes whether the second array
# is a valid subsequence of the first array. A valid subsequence of an array is classified as a set of numbers that
# aren’t necessarily adjacent in the array but are in the same order as they appear in the array. For example, [2, 5,
# 6] and [2, 6] are both considered as valid subsequences of the array [2, 3, 4, 5, 6]. It is also important to note
# that [2] and [2, 3, 4, 5, 6] are both valid subsequences of the array.
#
# Sample:
# Input array → [3, 6, 23, 7, 2, 4]
#
# Sequence → [3, 7, 4]
#
# Output → True

import unittest


def isValidSubsequence(array: list, sequence: list) -> bool:
    idx = 0
    for num in array:
        if num == sequence[idx]:
            idx += 1
        if idx == len(sequence):
            return True
    return False


class TestProgram(unittest.TestCase):
    def test_case_1(self) -> None:
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))


if __name__ == '__main__':
    test_case_1_obj = TestProgram()
    test_case_1_obj.test_case_1()
