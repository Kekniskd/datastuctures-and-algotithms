# You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.
#
# The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.
#
#
# Sample Input
# array = [2, 1, 2, 2, 2, 3, 4, 2]
# toMove = 2
#
# Sample Output
# [1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently

import unittest


def moveElementToEnd(array: list, toMove: int) -> list:
    i = 0
    j = len(array) - 1
    while j > i:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        expectedStart = [1, 3, 4]
        expectedEnd = [2, 2, 2, 2, 2]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:3])
        outputEnd = output[3:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)
