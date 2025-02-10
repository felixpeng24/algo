"""
Given a binary tree, return the level of the tree with minimum sum.
117
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#bfs pract, maybe make min([2,2,2,2])


def min_sum_level(root):
    if not root:
        return -1  # Return -1 if the tree is empty
    
    queue = [root]
    min_sum = float('inf')
    min_level = 0
    level = 0
    
    while queue:
        level_size = len(queue)
        level_sum = 0
        
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.value
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if level_sum < min_sum:
            min_sum = level_sum
            min_level = level
        
        level += 1
    
    return min_level





"""
    def minLevelSum(root):
        levelsum = []
        q = [root]
        while q:
            curr = q.pop(0)
"""