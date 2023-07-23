# You're given a binary expression tree. Write a function to evaluate this tree mathematically and return a single
# resulting integer.
#
# All leaf nodes in the tree represent operands, which will always be positive integers. All the other nodes
# represent operators. There are 4 operators supported, each of which is represented by a negative integer:
#
# -1:Addition operator, adding the left and right subtrees.
# -2: Subtraction operator, subtracting the right subtree from the left subtree.
# -3: Division operator, dividing the left subtree by the right subtree. If the result is a decimal, it should be rounded towards zero.
# -4: Multiplication operator, multiplying the left and right subtrees.
#
# You can assume the tree will always be a valid expression tree. Each operator also works as a grouping symbol,
# meaning the bottom of the tree is always evaluated first, regardless of the operator.
#
#
# Sample Input
# tree =    -1
#         /     \
#       -2       -3
#      /   \    /  \
#    -4     2  8    3
#   /   \
#  2     3
#
#
# Sample Output
# 6 // (((2 * 3) - 2) + (8 / 3))

import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree: BinaryTree) -> int:
    if tree.value >= 0:
        return tree.value

    left_value = evaluateExpressionTree(tree.left)
    right_value = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return left_value + right_value
    elif tree.value == -2:
        return left_value - right_value
    elif tree.value == -3:
        return int(left_value / right_value)
    else:
        return left_value * right_value


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(-1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(-2)
        tree.right.left = BinaryTree(5)
        tree.right.right = BinaryTree(1)
        expected = 6
        actual = evaluateExpressionTree(tree)
        self.assertEqual(actual, expected)
