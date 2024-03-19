# Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a one-dimensional array of all the array's elements in spiral order.
#
# Spiral order starts in the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral pattern all the way until every element has been visited.
#
#
# Sample Input
# array = [
#   [1,   2,  3, 4],
#   [12, 13, 14, 5],
#   [11, 16, 15, 6],
#   [10,  9,  8, 7],
# ]
#
# Sample Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

import unittest


def spiralTraverse(matrix):
    result = []
    while matrix:
        # Traverse top row
        result.extend(matrix.pop(0))

        # Traverse right column
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        # Traverse bottom row (in reverse)
        if matrix:
            result.extend(matrix.pop()[::-1])

        # Traverse left column (in reverse)
        if matrix and matrix[0]:
            for row in reversed(matrix):
                result.append(row.pop(0))

    return result


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(spiralTraverse(matrix), expected)
