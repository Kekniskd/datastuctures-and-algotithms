# Check if string has only unique characters

import unittest


def isUnique(input: str) -> str:
    hMap = {}

    for letter in input:
        hMap[letter] = hMap.get(letter, 0) + 1

    print(hMap)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = 'AaaaaaaaaaAAbcd'
        expected = False
        actual = isUnique(input)
        self.assertEqual(actual, expected)
