# Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common to all
# strings in the list, ignoring multiplicity.
# Note that the strings are not guaranteed to only contain alphanumeric characters. The list you return can be in any order.

# Sample Input
# strings = ["abc", "bcd", "cbaccd"]

# Sample Output
# ["b", "c"] // The characters could be ordered differently.

import unittest


def commonCharacters(strings: list) -> list:
    common_list = [i for i in strings[0]]
    for word in strings:
        temp = []
        for char in word:
            if char in common_list and char not in temp:
                temp.append(char)
        common_list = temp
    return common_list


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = ["abc", "bcd", "cbad"]
        expected = ["b", "c"]
        actual = commonCharacters(input)
        actual.sort()
        self.assertEqual(actual, expected)
