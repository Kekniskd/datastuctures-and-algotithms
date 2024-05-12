import unittest
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    lIdx = 1

    for idx in range(1, len(nums)):
        if nums[idx] != nums[idx - 1]:
            nums[lIdx] = nums[idx]
            lIdx += 1

    return lIdx


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = 5
        actual = removeDuplicates(input)
        self.assertEqual(actual, expected)
