"""
Given an array of positive integers, divide the array into two subsets such that 
the difference between the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, 
which has a difference of 5, which is the smallest possible difference.
"""

def min_difference_partition(arr):
    total_sum = sum(arr)
    n = len(arr)
    target = total_sum // 2

    # dp[i] means: is sum i achievable
    dp = [False] * (target + 1)
    dp[0] = True

    # To reconstruct the set
    prev = {0: set()}

    for num in arr:
        new_dp = dp[:]
        new_prev = prev.copy()
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                new_dp[s] = True
                new_prev[s] = prev[s - num] | {num}
        dp = new_dp
        prev = new_prev

    # Find the best achievable subset sum ≤ target
    for i in range(target, -1, -1):
        if dp[i]:
            subset1 = prev[i]
            subset2 = set(arr) - subset1
            return subset1, subset2, abs(sum(subset1) - sum(subset2))

# Example usage
arr = [5, 10, 15, 20, 25]
subset1, subset2, diff = min_difference_partition(arr)
print("Subset 1:", subset1)
print("Subset 2:", subset2)
print("Difference:", diff)
