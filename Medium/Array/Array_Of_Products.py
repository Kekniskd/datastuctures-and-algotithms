# Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.
#
# In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].
#
# Note that you're expected to solve this problem without using division.
#
#
# Sample Input
# array = [5, 1, 4, 2]
#
# Sample Output
# [8, 40, 10, 20]
# // 8 is equal to 1 x 4 x 2
# // 40 is equal to 5 x 4 x 2
# // 10 is equal to 5 x 1 x 2
# // 20 is equal to 5 x 1 x 4


import unittest


# Very slow approach
def arrayOfProducts_1(array: list) -> list:
    array_copy = [0 for _ in array]
    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if j == i:
                continue
            else:
                product *= array[j]
        array_copy[i] = product

    return array_copy


def arrayOfProducts(array: list) -> list:
    res = [1 for _ in array]
    for i in range(1, len(array)):
        res[i] = res[i - 1] * array[i - 1]
    postfix = 1
    for i in range(len(array) - 1, -1, -1):
        res[i] *= postfix
        postfix *= array[i]
    return res


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 4, 2]
        expected = [8, 40, 10, 20]
        actual = arrayOfProducts(array)
        self.assertEqual(actual, expected)
