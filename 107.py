"""
This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / 
2   3
   / 
  4   5

"""

# bfs, using queue and pops

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def bfs(root):
    q = [root]
    visited = []

    while q:
      curr = q.pop0
      visited.add(curr)
      if curr.right:
        q.append(curr.left)
      if curr.left:
        q.append(curr.right)
    
    return visited
    
