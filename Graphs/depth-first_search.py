# You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form an
# acyclic tree-like structure. Implement the depthFirstSearch method on the Node class, which takes in an empty
# array, traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to
# right), stores all the nodes' names in the input array, and returns it.
#
# If you're unfamiliar with Depth-first Search, we recommend watching the Conceptual Overview section of this
# question's video explanation before starting to code.
#
#
# Sample Input
# graph = A
#      /  |  \
#     B   C   D
#    / \     / \
#   E   F   G   H
#      / \   \
#     I   J   K
#
# Sample Output
# ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

import unittest


class Node:
    def __init__(self, name: str):
        self.children = []
        self.name = name

    def addChild(self, name: str):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array: list):

        if not self.children:
            return
        else:
            array.append(self.name)
            for child in self.children:
                self.depthFirstSearch(child)

        return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.depthFirstSearch([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])
