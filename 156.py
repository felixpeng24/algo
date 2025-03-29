"""
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.

"""

# go from biggest squarev value that is still equvalent, subtract, and go down the list of combinations since you want the smallest list?

import math

def min_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 can be represented with 0 squares
    
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
            
    return dp

# Example cases
print(min_squares(13))  # Output: 2
