"""
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


# Example 1:
# Input: coins = [3,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

"""

def coinChange(coins, amount):
    # Initialize dp array where dp[i] = min number of coins to make amount i
    # Start with amount + 1 (a value greater than any possible answer)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make amount 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1
