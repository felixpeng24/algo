"""

This problem was asked by Yelp.

You are given an array of integers, where each element represents the maximum number of steps
that can be jumped going forward from that element. Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2,
 as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.
"""

# dp, you have two choices: jump or dont jump
# so we start at 6, meaning we have 6 decisions stemming from that: 2, 4, 0, 5, 1, 1
"""
maybe start backwards? so how do we get to 9, what are the best steps to take?
[6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
look at 2, we can get to 9 in 1 step
look at 4, get to 9 in 1 step
look at 1, get to 9 in 2 steps (move to 4, then another step)
look at 1, get to 9 in 3 steps
look at 5, get to 9 in 1 step
look at 0, maybe a special case so we dont choose or we get stuck
look at 4, find 1+ min(steps for 5, 1, 1), which is 1+1 = 2
continue

"""

def minSteps(nums):
    dp = [0] * (len(nums) - 1)
    for i in range(len(nums)-2, -1, -1): #start at 2, go backwards
        # goal = len(nums) = 10
        # current step = i + 1
        steps_needed = len(nums) - (i + 1)
        if nums[i] >= steps_needed:
            dp[i] = 1
        else:
            if nums[i] == 0:
                dp[i] = float('inf')
            for k in range(1, nums[i]+1):