"""
In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     
  2         3
 / \       / 
4   5     6   7
"""

#bfs right off the bat, jsut have to alternate

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
def boust(root):
    q = [root]
    res = []
    is_left = False
    while q:
        curr = q.pop(0)
        res.append(curr.val)
        if is_left:
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            is_left = False
        else:
            if curr.left:
                q.append(curr.right)
            if curr.right:
                q.append(curr.left)
            is_left = True
    
    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(boust(root))

#lets do level order traversal

from collections import deque

def boustrophedon_order(root):
    if not root:
        return []

    res = []
    q = deque([root])
    left_to_right = True

    while q:
        level_size = len(q)
        level = []

        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if not left_to_right:
            level.reverse()
        res.extend(level)
        left_to_right = not left_to_right

    return res
