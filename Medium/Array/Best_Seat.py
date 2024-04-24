# You walk into a theatre you're about to see a show in. The usher within the theatre walks you to your row and mentions you're allowed to sit anywhere within the given row. Naturally you'd like to sit in the seat that gives you the most space. You also would prefer this space to be evenly distributed on either side of you (e.g. if there are three empty seats in a row, you would prefer to sit in the middle of those three seats).
#
# Given the theatre row represented as an integer array, return the seat index of where you should sit. Ones represent occupied seats and zeroes represent empty seats.
#
# You may assume that someone is always sitting in the first and last seat of the row. Whenever there are two equally good seats, you should sit in the seat with the lower index. If there is no seat to sit in, return -1. The given array will always have a length of at least one and contain only ones and zeroes.
#
#
# Sample Input
# seats = [1, 0, 1, 0, 0, 0, 1]
#
# Sample Output
# 4

import unittest


def bestSeat_(seats: list) -> int:
    maxSpace = 0
    bestSeatIdx = -1
    left = 0

    while left < len(seats):
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right += 1
        currSpace = right - left - 1
        if currSpace > maxSpace:
            maxSpace = currSpace
            bestSeatIdx = (right + left) // 2

        left = right

    return bestSeatIdx


def bestSeat(seats: list) -> int:
    maxSpace = 0
    bestSeatIdx = -1
    currSpace = 0

    for idx in range(len(seats)):
        if not seats[idx]:
            currSpace += 1
        else:
            if currSpace > maxSpace:
                maxSpace = currSpace
                bestSeatIdx = idx - 1 - currSpace // 2
            currSpace = 0

    return bestSeatIdx


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 0, 1, 0, 0, 0, 1]
        expected = 4
        actual = bestSeat(input)
        self.assertEqual(actual, expected)
