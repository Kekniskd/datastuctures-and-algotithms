# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
# non-decreasing order

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

import unittest


def sortedSquaredArray(array: list) -> list:
    l_idx = 0
    r_idx = len(array) - 1
    out_idx = len(array) - 1
    sqr_arr = [0 for _ in array]
    while l_idx <= r_idx:
        if abs(array[l_idx]) > abs(array[r_idx]):
            sqr_arr[out_idx] = array[l_idx] * array[l_idx]
            l_idx += 1

        elif array[l_idx] < array[r_idx]:
            sqr_arr[out_idx] = array[r_idx] * array[r_idx]
            r_idx -= 1
        out_idx -= 1
    return sqr_arr


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [1, 2]
        expected = [1, 4]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    test_case_1_obj = TestProgram()
    test_case_1_obj.test_case_1()
