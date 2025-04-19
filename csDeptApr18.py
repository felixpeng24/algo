"""
96. Unique Binary.
Search Trees
Given an integer n, return the
number of structurally
unique BST's (binary search
trees) which has exactly n
nodes of unique values from 1
to n.

"""

#left smaller, right bigger
#since theres n, i wonder if we could do memoization?
#or bottom up approach, where...


def numTrees(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1  # Base cases

    for nodes in range(2, n + 1):
        for root in range(1, nodes + 1):
            dp[nodes] += dp[root - 1] * dp[nodes - root]
    
    return dp[n]

#this is insanity ngl