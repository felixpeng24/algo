"""
Given a binary tree, return the level of the tree with minimum sum.
117
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#bfs pract

    def minLevelSum(root):
