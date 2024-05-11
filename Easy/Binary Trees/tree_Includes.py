# Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether the value is contained in the tree.

from typing import Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_includes(root: Optional[TreeNode], target: str) -> bool:
    """
    Depth First Trivalrsel solution
    """
    if root is None:
        return False
    if root.val == target:
        return True

    return tree_includes(root.left, target) or tree_includes(root.right, target)


# def tree_includes(root: Optional[TreeNode], target: str) -> bool:
#     """
#     Breadth First Trivalrsel solution
#     """
#     queue = [root]
#     while queue:
#         curr = queue.pop(0)
#         if curr.val == target:
#             return True
#         if curr.left is not None:
#             queue.append(curr.left)
#         if curr.right is not None:
#             queue.append(curr.right)
#
#     return False


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        a = TreeNode("a")
        b = TreeNode("b")
        c = TreeNode("c")
        d = TreeNode("d")
        e = TreeNode("e")
        f = TreeNode("f")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f

        actual = tree_includes(a, "b")
        expected = True
        self.assertEqual(actual, expected)
