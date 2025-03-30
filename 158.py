"""
This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, 
how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a 
wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

"""
#keep going right, then down 1, then all the way right on 1st iteration
#remember # of steps, then subtract 1 from the first right to go down 1 a step earlier, repeat for the rest

def count_paths(matrix):
    if not matrix or matrix[0][0] == 1:
        return 0  # If start is blocked, no path exists.

    N, M = len(matrix), len(matrix[0])
    dp = [[0] * M for _ in range(N)]
    
    # Initialize start position
    dp[0][0] = 1

    # Fill DP table
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                dp[i][j] = 0  # Wall, no path
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]  # From top
                if j > 0:
                    dp[i][j] += dp[i][j-1]  # From left

    return dp[N-1][M-1]  # Paths to bottom-right

# Example usage:
matrix = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0]
]
print(count_paths(matrix))  # Output: 2
