# Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that returns a new string
# obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key.
#
# Note that letters should "wrap" around the alphabet; in other words, the letter z shifted by one returns the letter a.
#
# Sample Input
# string = "xyz"
# key = 2
#
# Sample Output
# "zab"


import unittest


def caesarCipherEncryptor(string: str, key: int) -> str:
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)


def getNewLetter(letter: str, key: int) -> str:
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesarCipherEncryptor("xyz", 2), "zab")