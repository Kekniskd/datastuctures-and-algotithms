# Write a function that takes in a non-empty string and returns its run-length encoding.
#
# From Wikipedia, ("run-length encoding is a form of lossless data compression in which runs of data are stored as a single data value and
# count,"
# " rather than as the original run.") For this problem, a run of data is any sequence of consecutive, identical characters.
# So the run "AAA" would be run-length-encoded as "3A".
#
# To make things more complicated, however, the input string can contain all sorts of special characters, including numbers. And since encoded
# data must be decodable, this means that we can't naively run-length-encode long runs. For example, the run "AAAAAAAAAAAA" (12 As), can't
# naively be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA" or "1AA". Thus, long runs (runs of 10 or more
# characters) should be encoded in a split fashion; the aforementioned run should be encoded as "9A3A".
#
# Sample Input
# string = "AAAAAAAAAAAAABBCCCCDD"
#
# Sample Output
# "9A4A2B4C2D"

import unittest


def runLengthEncoding(string: str) -> str:
    encoded = ''
    count = 0
    curr = string[0]
    for idx in range(len(string)):
        if string[idx] == curr and count < 9:
            count += 1
        else:
            encoded = encoded + str(count) + curr
            curr = string[idx]
            count = 1
    encoded = encoded + str(count) + curr
    return encoded


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "AAAAAAAAAAAAABBCCCCDD"
        expected = "9A4A2B4C2D"
        actual = runLengthEncoding(string)
        self.assertEqual(actual, expected)
