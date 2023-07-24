# You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values. Write a function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values. The Linked List should be modified in place (i.e., you shouldn't create a brand-new list), and the modified Linked List should still have its nodes sorted with respect to their values.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.
#
# Sample Input
# linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 // the head node with value 1
#
# Sample Output
# 1 -> 3 -> 4 -> 5 -> 6 // the head node with value 1

import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


def removeDuplicatesFromLinkedList(linkedList: LinkedList) -> LinkedList:
    curr_node = linkedList
    while curr_node.next is not None:
        if curr_node.value == curr_node.next.value:
            curr_node.next = curr_node.next.next
        else:
            curr_node = curr_node.next

    return linkedList


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
        expected = LinkedList(1).addMany([3, 4, 5, 6])
        actual = removeDuplicatesFromLinkedList(test)
        self.assertEqual(actual.getNodesInArray(), expected.getNodesInArray())
