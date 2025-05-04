r"""
Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum 
of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.

"""

#def dfs
from collections import defaultdict

class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def frequentSubtree(root):
    freqList = defaultdict(int)

    def dfs(root):
        if not root:
            return 0
        curr = root.val + dfs(root.left) + dfs(root.right)
        freqList[curr] += 1
        return curr
    
    dfs(root)
    max_freq = max(freqList.values())

    for key, values in freqList.items():
        if values == max_freq:
            return key
