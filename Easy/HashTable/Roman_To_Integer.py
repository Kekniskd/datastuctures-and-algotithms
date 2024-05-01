import unittest


def romanToInt(s: str) -> int:
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0

    for i in range(len(s)):
        if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
            ans -= m[s[i]]
        else:
            ans += m[s[i]]

    return ans


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        roman = "III"
        expected = 3
        actual = romanToInt(roman)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        roman = "LVIII"
        expected = 58
        actual = romanToInt(roman)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        roman = "MCMXCIV"
        expected = 1994
        actual = romanToInt(roman)
        self.assertEqual(expected, actual)
