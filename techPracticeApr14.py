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






# lets try this prob agaib

"""
Given the root of a binary tree, return the level order traversal of its nodes' 
values. (i.e., from left to right, level by level).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[null, null, 15,7]]

"""

# we can implement ez using bfs, but what if we dont want to use another data structure

#i remember we did need height of tree, so lets grab that rq

def height(node):
    if not node:
        return 0
    
    return 1+max(node.left, node.right)

def treeTraverse(node):
    h = height(node)
    res = []

    def dfs(level, node):
        if not node:
            return None
        return [dfs(level-1, node.left), dfs(level-1, node.right)]
    for level in range(h+1):
        currLevel = []
        for _ in 


        res.append(currLevel)