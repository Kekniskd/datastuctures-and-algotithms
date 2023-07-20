# The distance between a node in a Binary Tree and the tree's root is called the node's depth.
#
# Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.
#
# Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be
# BinaryTree nodes themselves or None / null.
#
# Sample Input
# tree =    1
#        /     \
#       2       3
#     /   \   /   \
#    4     5 6     7
#  /   \
# 8     9

# Sample Output
# 16
# // The depth of the node with value 2 is 1.
# // The depth of the node with value 3 is 1.
# // The depth of the node with value 4 is 2.
# // The depth of the node with value 5 is 2.
# // Etc..
# // Summing all of these depths yields 16.

import unittest


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root: BinaryTree, depth: int = 0) -> int:
    # Write your code here.
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        actual = nodeDepths(root)
        self.assertEqual(actual, 16)
