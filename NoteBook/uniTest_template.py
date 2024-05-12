import unittest


def dummy(input: str) -> str:
    return input


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = 'A'
        expected = 'A'
        actual = dummy(input)
        self.assertEqual(actual, expected)
