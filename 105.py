"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal 
to target. If there is no such subarray, return 0 instead.
"""

def minSubArrayLen(target, nums):
#sliding window
    l = 0
    curr = 0
    minlength = 0
    for r in range(len(nums)):
        curr += nums[r]
        while curr >= target:
            minlength = min(minlength, r - l + 1)
            curr -= nums[l]
            l += 1
    return minlength

