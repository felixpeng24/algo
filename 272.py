"""
Write a function, throw_dice(N, faces, total), that determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
"""
def throw_dice(N, faces, total):
    # Initialize a 2D DP array with (N+1) x (total+1) size
    dp = [[0] * (total + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: 1 way to reach 0 total with 0 dice

    for n in range(1, N + 1):  # For each number of dice
        for t in range(1, total + 1):  # For each possible total
            for f in range(1, faces + 1):  # Try each face value
                if t - f >= 0:
                    dp[n][t] += dp[n - 1][t - f]

    return dp[N][total]
