# You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix. The
# transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from
# top-left to bottom-right); it switches the row and column indices of the original matrix. You can assume the input
# matrix always has at least 1 value; however its width and height are not necessarily the same.

# Sample Input #1
# matrix = [
#   [1, 2],
# ]
#
# Sample Output # 1
# [
#   [1],
#   [2]
# ]

import unittest


def transposeMatrix(matrix):
    trans_matrx = []
    for i in range(len(matrix[0])):
        trans_mat = []
        for mat in matrix:
            trans_mat.append(mat[i])
        trans_matrx.append(trans_mat)
    return trans_matrx


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        actual = transposeMatrix(input)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    test_case_1_obj = TestProgram()
    test_case_1_obj.test_case_1()
