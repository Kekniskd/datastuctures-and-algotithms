# Write a function that takes in an array of at least three integers and, without sorting the input array, returns a sorted array of the
# three largest integers in the input array.
#
# The function should return duplicate integers if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
#
# Sample Input
# array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
#
# Sample Output
# [18, 141, 541]

import unittest


def findThreeLargestNumbers(array: list) -> list:
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest


def updateLargest(threeLargest: list, num: int) -> None:
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)


def shiftAndUpdate(array: list, num: int, idx: int) -> None:
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]),
            [18, 141, 541],
        )

    def test_case_2(self):
        self.assertEqual(
            findThreeLargestNumbers([2, 1, 0]),
            [0, 1, 2],
        )

