r"""
Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8

"""

# check if valid bst by passing down the bounds
#dfs 

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_bst_from_postorder(postorder):
    def helper(lower, upper):
        nonlocal index
        if index < 0:
            return None
        val = postorder[index]
        if not (lower < val < upper):
            return None
        
        index -= 1
        root = TreeNode(val)
        # Build right first (reverse of postorder)
        root.right = helper(val, upper)
        root.left = helper(lower, val)
        return root

    index = len(postorder) - 1
    return helper(float('-inf'), float('inf'))
