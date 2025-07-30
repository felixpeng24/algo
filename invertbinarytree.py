"""
Invert Binary tree

"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def invertBinTree(root):
    
    def invertChild(node):

        if node == None:
            return None
        left = invertChild(node.left)
        right = invertChild(node.right)
        node.left = right
        node.right = left
        return node
    
    return invertChild(root)
