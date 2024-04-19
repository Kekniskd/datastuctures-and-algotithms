# Write a function that takes in an array of integers and returns the length of the longest peak in the array.
#
# A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.
#
# For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.
#
#
# Sample Input
# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
#
# Sample Output
# 6 // 0, 10, 6, 5, -1, -3

import unittest


def longestPeak(array: list) -> int:
    idx = 1
    longestPeakNum = 0
    currLongestPeak = 0
    while idx <= len(array) - 2:
        if array[idx - 1] < array[idx] < array[idx + 1]:
            currLongestPeak += 1
            idx += 1
        elif array[idx] > array[idx - 1] and array[idx] > array[idx + 1]:
            currLongestPeak += 2
            idx += 1
            for slopeIdx, slope in enumerate(array[idx:], start=idx):
                if slope >= array[slopeIdx - 1]:
                    idx = slopeIdx
                    if currLongestPeak > longestPeakNum:
                        longestPeakNum = currLongestPeak
                        currLongestPeak = 0
                        break
                    currLongestPeak = 0
                    break
                elif slopeIdx == len(array) - 1:
                    currLongestPeak += 1
                    if currLongestPeak > longestPeakNum:
                        longestPeakNum = currLongestPeak
                        currLongestPeak = 0
                else:
                    currLongestPeak += 1
        else:
            idx += 1
            currLongestPeak = 0
    return longestPeakNum


def longestPeak_2(array: list) -> int:
    longest_peak_length = 0
    i = 1

    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]

        if not is_peak:
            i += 1
            continue

        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1

        right = i + 2
        while right < len(array) and array[right] < array[right - 1]:
            right += 1

        current_peak_length = right - left - 1
        longest_peak_length = max(longest_peak_length, current_peak_length)

        i = right

    return longest_peak_length


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected = 6
        self.assertEqual(longestPeak(array), expected)

    def test_case_2(self):
        array = [1, 3, 2]
        expected = 3
        self.assertEqual(longestPeak(array), expected)
