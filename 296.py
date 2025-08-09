"""
Given a sorted array, convert it into a height-balanced binary search tree.
"""

#start in middle, place as root, recursive two sides and attach to higher node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    def build(l, r):
        if l > r:
            return None
        mid = (l + r) // 2          # choose middle
        root = TreeNode(nums[mid])
        root.left  = build(l, mid - 1)
        root.right = build(mid + 1, r)
        return root
    return build(0, len(nums) - 1)
