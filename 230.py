"""
goldman sachs, medium 

You are given N identical eggs and access to a building with k floors. 
Your task is to find the lowest floor that will cause an egg to break, 
if dropped from that floor. Once an egg breaks, it cannot be dropped again.
If an egg breaks when dropped from the xth floor, you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor, 
beginning with the first, until we reach the fifth floor, so our solution will be 5.

"""
#binary search for the floor, start with middle floor
#jk its a dp problem with a 2x2 table to test, similar to coin change

def egg_drop(N, K):
    # Create DP table: (N+1) x (K+1)
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    # Base cases:
    for k in range(K + 1):
        dp[1][k] = k  # 1 egg: must try every floor

    for n in range(1, N + 1):
        dp[n][0] = 0  # 0 floors needs 0 trials
        dp[n][1] = 1  # 1 floor needs 1 trial

    # Fill the DP table
    for n in range(2, N + 1):
        for k in range(2, K + 1):
            dp[n][k] = float('inf')  # Initialize to infinity
            for x in range(1, k + 1):
                drops = 1 + max(dp[n - 1][x - 1], dp[n][k - x])
                if drops < dp[n][k]:
                    dp[n][k] = drops

    return dp[N][K]
