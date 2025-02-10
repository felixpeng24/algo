"""
Given an integer list where each number represents the number of hops you can make, determine
 whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""

# brute force solution? could ask more clarifying qs like if the numbers stack

def reachCheckpoint(nums):
    fuel = 0
    for num in nums:
        if fuel < 0:
            return False
        else:
            fuel -= 1
            fuel += num
    return True