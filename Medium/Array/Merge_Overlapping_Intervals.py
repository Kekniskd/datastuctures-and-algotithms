# Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals, and returns the new intervals in no particular order.
#
# Each interval is an array of two integers, with interval[0] as the start of the interval and interval[1] as the end of the interval.
#
# Note that back-to-back intervals aren't considered to be overlapping. For example, [1, 5] and [6, 7] aren't overlapping; however, [1, 6] and [6, 7] are indeed overlapping.
#
# Also note that the start of any particular interval will always be less than or equal to the end of that interval.
#
# Sample Input
# intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
# Sample Output
# [[1, 2], [3, 8], [9, 10]]
# // Merge the intervals [3, 5], [4, 7], and [6, 8].
# // The intervals could be ordered differently.

import unittest


def mergeOverlappingIntervals(intervals: list) -> list:
    intervals.sort(key=lambda inter: inter[0])
    res = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= res[-1][1]:
            res[-1] = [res[-1][0], max(interval[1], res[-1][1])]
        else:
            res.append(interval)
    return res


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
        expected = [[1, 2], [3, 8], [9, 10]]
        actual = mergeOverlappingIntervals(intervals)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
        expected = [[1, 10]]
        actual = mergeOverlappingIntervals(intervals)
        self.assertEqual(actual, expected)
