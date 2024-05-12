import unittest


def lengthOfLongestSubstring(s: str) -> int:
    lPointer = 0
    rpointer = 1
    while rpointer < len(s) - 1:
        if s[rpointer] != s[lPointer]:
            rpointer += 1
        if s[rpointer] == s[lPointer]:
            lPointer += 1

    return rpointer - lPointer - 1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "abcabcbb"
        expected = 3
        actual = lengthOfLongestSubstring(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = "bbbbb"
        expected = 1
        actual = lengthOfLongestSubstring(input)
        self.assertEqual(actual, expected)
