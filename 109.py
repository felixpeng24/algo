"""
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  /
 2   3
    /
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].


"""

#dfs?

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_path(root):
    def dfs(node, path, result):
        if not node:
            return None
        path.append(node.value)
        if node.left == None and node.right == None:
            result.append(list(path))
        else:
            dfs(node.left, path, result)
            dfs(node.right, path result)
        path.pop()

    result = []
    dfs(root, [], result)
    return result