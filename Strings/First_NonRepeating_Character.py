# Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first non-repeating character.
# The first non-repeating character is the first character in a string that occurs only once.
# If the input string doesn't have any non-repeating characters, your function should return -1

# Sample Input
# string = "abcdcaf"

# Sample Output
# 1 // The first non-repeating character is "b" and is found at index 1.

import unittest


def firstNonRepeatingCharacter(string: str) -> int:
    for idx in range(len(string)):
        dublicate = False
        for idx2 in range(len(string)):
            if string[idx] == string[idx2] and idx != idx2:
                dublicate = True

        if not dublicate:
            return idx
    return -1


def firstNonRepeatingCharacter2(string):
    characterFrequencies = {}
    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1
    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx
    return -1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "abcdcaf"
        expected = 1
        actual = firstNonRepeatingCharacter(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = "abcdcaf"
        expected = 1
        actual = firstNonRepeatingCharacter2(input)
        self.assertEqual(actual, expected)
