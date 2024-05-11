from typing import Optional, List
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def breadFirstSearch(root: Optional[TreeNode]) -> Optional[List]:
    if root is None:
        return []
    res = []
    queue = [root]
    while queue:
        curr = queue.pop(0)
        res.append(curr.val)
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)

    return res


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
        expected = ['a', 'b', 'c', 'd', 'e', 'f']
        actual = breadFirstSearch(a)
        self.assertEqual(actual, expected)
        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f

    def test_case_2(self):
        a = None
        expected = []
        actual = breadFirstSearch(a)
        self.assertEqual(actual, expected)
