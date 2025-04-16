"""
Given the root of a binary tree, return the level order traversal of its nodes' 
values. (i.e., from left to right, level by level).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[null, null, 15,7]]

"""
from collections import deque

class TreeNode:
    def __init__(self, value, left, right):
        self.val = value
        self.left = left
        self.right = right


def levelOrderBFS(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    
    return result


def levelOrder(root):
    def height(node):
        if not node.left or not node.right:
            return 1
        return 1+max(height(node.left),height(node.right))
    
    def getLevel(node, level, result):
        if not node:
            return
        if level == 1:
            result.append(node.val)
        elif level > 1:
            getLevel(node.left, level - 1, result)
            getLevel(node.right, level - 1, result)

    
    h = height(root)
    final = []
    for level in range(1, h+1):
        level_result = []
        getLevel(root, level, level_result)
        final.append(level_result)
