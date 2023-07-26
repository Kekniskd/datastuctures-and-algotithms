# You're given a Linked List with at least one node. Write a function that returns the middle node of the Linked List. If there are two middle nodes (i.e. an even length list), your function should return the second of these nodes.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.
#
# Sample Input
# linkedList = 2 -> 7 -> 3 -> 5
#
# Sample Output
# 3 -> 5 // The middle could be 7 or 3,
# // we return the second middle node

import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList: LinkedList) -> LinkedList:
    lenth = 0
    curr = linkedList
    while curr is not None:
        lenth += 1
        curr = curr.next

    curr = linkedList
    for _ in range(lenth // 2):
        curr = curr.next
    return curr


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedList = LinkedList(0)
        linkedList.next = LinkedList(1)
        expected = LinkedList(2)
        linkedList.next.next = expected
        expected.next = LinkedList(3)
        actual = middleNode(linkedList)
        self.assertEqual(actual, expected)
