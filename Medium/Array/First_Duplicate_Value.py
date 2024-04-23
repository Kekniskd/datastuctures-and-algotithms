# Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that returns the first integer that appears more than once (when the array is read from left to right).
#
# In other words, out of all the integers that might occur more than once in the input array, your function should return the one whose first duplicate value has the minimum index.
#
# If no integer appears more than once, your function should return -1.
#
# Note that you're allowed to mutate the input array.
#
#
# Sample Input #1
# array = [2, 1, 5, 2, 3, 3, 4]
#
# Sample Output #1
# 2 // 2 is the first integer that appears more than once.
# // 3 also appears more than once, but the second 3 appears after the second 2.
#
#
# Sample Input #2
# array = [2, 1, 5, 3, 3, 2, 4]
#
# Sample Output #2
# 3 // 3 is the first integer that appears more than once.
# // 2 also appears more than once, but the second 2 appears after the second 3.


import unittest


# Space compexity is O(n) we can do O(1)
def firstDuplicateValue(array: list) -> int:
    # Write your code here.
    seen = set()
    for num in array:
        if num in seen:
            return num
        seen.add(num)
    return -1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        actual = firstDuplicateValue(input)
        self.assertEqual(actual, expected)
