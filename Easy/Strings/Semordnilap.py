# Write a function that takes in a list of unique strings and returns a list of semordnilap pairs.
#
# A semordnilap pair is defined as a set of different strings where the reverse of one word is the same as the forward version of the other. For example the words "diaper" and "repaid" are a semordnilap pair, as are the words "palindromes" and "semordnilap".
#
# The order of the returned pairs and the order of the strings within each pair does not matter.
#
# Sample Input
# words = ["diaper", "abc", "test", "cba", "repaid"]
#
# Sample Output
# [["diaper", "repaid"], ["abc", "cba"]]

import unittest


def semordnilap(words: list) -> list:
    wordsSet = set(words)
    semordnilapPairs = []

    for word in words:
        reverse = word[::-1]
        if reverse in wordsSet and reverse != word:
            semordnilapPairs.append([word, reverse])
            wordsSet.remove(word)
            wordsSet.remove(reverse)

    return semordnilapPairs


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = ["desserts", "stressed", "hello"]
        expected = [["desserts", "stressed"]]
        actual = semordnilap(input)
        self.assertEqual(actual, expected)
