from typing import Optional, List
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def depth_first_values(root: Optional[TreeNode]) -> List[int]:
#     result = []
#     stack = [root]
#     while stack:
#         curr = stack.pop()
#         result.append(curr.val)
#         if curr.right is not None:
#             stack.append(curr.right)
#         if curr.left is not None:
#             stack.append(curr.left)
#     return result


def depth_first_values(root: Optional[TreeNode]) -> Optional[List]:
    if root is None:
        return []
    return [root.val] + depth_first_values(root.left) + depth_first_values(root.right)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        a = TreeNode('a')
        b = TreeNode('b')
        c = TreeNode('c')
        d = TreeNode('d')
        e = TreeNode('e')
        f = TreeNode('f')
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        expected = ['a', 'b', 'd', 'e', 'c', 'f']
        actual = depth_first_values(a)
        self.assertEqual(actual, expected)

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
