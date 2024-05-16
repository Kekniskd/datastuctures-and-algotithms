import unittest


def alternativeSequence(array: list) -> int:
    if len(array) == 0:
        return 0

    currLen = 1
    maxLen = 0

    for idx in range(1, len(array)):
        if array[idx] != array[idx - 1]:
            currLen += 1
        else:
            maxLen = max(maxLen, currLen)
            currLen = 1

    maxLen = max(maxLen, currLen)
    return maxLen


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1]
        expected = 7
        actual = alternativeSequence(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0]
        expected = 7
        actual = alternativeSequence(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = []
        expected = 0
        actual = alternativeSequence(input)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        input = [1]
        expected = 1
        actual = alternativeSequence(input)
        self.assertEqual(actual, expected)
