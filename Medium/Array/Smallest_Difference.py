# Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.
#
# Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.
#
# You can assume that there will only be one pair of numbers with the smallest difference.
#
#
# Sample Input
# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]
#
# Sample Output
# [28, 26]


import unittest


def smallestDifference(arrayOne: list, arrayTwo: list) -> list:
    arrayOne.sort()
    arrayTwo.sort()
    smallest = float("inf")
    idx_1 = 0
    idx_2 = 0
    pair = []
    while idx_1 < len(arrayOne) and idx_2 < len(arrayTwo):
        one_num = arrayOne[idx_1]
        two_num = arrayTwo[idx_2]
        if one_num > two_num:
            curr = one_num - two_num
            idx_2 += 1
        elif two_num > one_num:
            curr = two_num - one_num
            idx_1 += 1
        else:
            return [one_num, two_num]
        if smallest > curr:
            smallest = curr
            pair = [one_num, two_num]
    return pair


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26]
        )
