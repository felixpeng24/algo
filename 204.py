r"""
Given a complete binary tree, count the number of nodes in faster than O(n) time. 
Recall that a complete binary tree has every level filled except the last, 
and the nodes in the last level are filled starting from the left.

        1
       / \
      2   3
      /\  /\
      4 5 6 7 

"""

     

#traverse starting from left, count number of nodes to get thre, count from left

class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def count_nodes(root):
    def height(node):
        h = 1
        while node.left:
            h += 1
            node = node.left
    
    h = height(root)

def count_last_level_nodes(root, height):
    # Binary search range for the last level nodes
    left, right = 0, 2**height - 1
    while left <= right:
        mid = (left + right) // 2
        if node_exists(root, height, mid):
            # If the node exists at index mid, search for more nodes on the right
            left = mid + 1
        else:
            # If the node doesn't exist, search the left half
            right = mid - 1
    return left

# Helper function to check if a node exists at a specific index at the last level
def node_exists(root, height, index):
    # Perform binary traversal to find the node at the given index
    left, right = 0, 2**height - 1
    current = root
    for i in range(height):
        mid = (left + right) // 2
        if index <= mid:
            # Traverse left subtree
            current = current.left
            right = mid
        else:
            # Traverse right subtree
            current = current.right
            left = mid + 1
    return current is not None
