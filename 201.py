"""
You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers.
 For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, 
eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.

"""

#brute force bvy going through every path

#or dp? lemme think how this would work, backtrakcing from bottom up

def max_path_sum(triangle):
    # Copy the last row as the initial state of our dp array
    dp = triangle[-1][:]
    
    # Start from the second-to-last row, moving upward
    for row in reversed(triangle[:-1]):
        for i in range(len(row)):
            # Update dp[i] to be the max path sum at that position
            dp[i] = row[i] + max(dp[i], dp[i + 1])
    
    return dp[0]

# Example usage
triangle = [[1], [2, 3], [1, 5, 1]]
print(max_path_sum(triangle))  # Output: 9

#we were close