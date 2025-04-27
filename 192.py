"""

You are given an array of nonnegative integers. 
Let's say you start at the beginning of the array and are trying to advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], 
we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""
#diff paths using dp
#what would backtrack approach do? start from end, you need 1 step in n-1, 2 in n-2, etc

def can_reach_end(nums):
    max_reach = 0
    for i, steps in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + steps)
    return True

nums = [1, 3, 2, 1, 0, 0]
print(can_reach_end(nums))


def jumpgame(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i+nums[i])
    
    return True
