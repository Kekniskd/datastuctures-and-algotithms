# Write a function that takes in a Binary Search Trees (BST) and a target integer value and returns the closest value
# to that target value contained in the BST. You can assume that there will only be one closest value. Each BST node
# has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only
# if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its
# value is less than or equal to the values of every node to its right; and its children nodes are either valid BST
# nodes themselves or None / null.


import unittest


def findClosestValueInBst(tree, target):
    currClosest = tree.value
    curr = tree

    while curr:
        print(curr.value)
        curr_diffrance = abs(target - curr.value)
        closest_diffrance = abs(target - currClosest)

        if curr_diffrance < closest_diffrance:
            currClosest = curr.value

        if target > curr.value:
            curr = curr.right
        elif target < curr.value:
            curr = curr.left

        else:
            break

    return currClosest


def findClosestValueInBst(tree, target):
    return helper(tree, target, tree.value)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if tree.value > target:
        return helper(tree.left, target, closest)
    elif tree.value < target:
        return helper(tree.right, target, closest)
    else:
        return closest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        actual = findClosestValueInBst(root, 12)
        self.assertEqual(expected, actual)
