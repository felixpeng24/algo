"""
This problem was asked by PayPal.

Given a binary tree, determine whether or not it is height-balanced.
 A height-balanced binary tree can be defined as one in which the heights of the two subtrees of any node never differ by more than one.
"""

#dfs, find the height of every path and check if theyre all within one of eachother
        # curr_height = 0
        # if not node:
        #     return heights.append(curr_height)
        # return 1 + d
            # heights = []
def heightBalance(root):

    def dfs(node):


        if not node:
            return 0
        return [1 + max(dfs(node.left), dfs(node.right)), 1 + min(dfs(node.left), dfs(node.right))]
    
    if abs(dfs(root)[0] - dfs(root)[1]) <= 1:
        return True
    return False