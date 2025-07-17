"""
easy

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, 
return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
"""

def fixed(nums):
    for i in range(len(nums)):
        if i == nums[i]:
            return i

    return False

#ah but array is sorted, so should set of binary search alarms

def bsfixed(nums):
    l, r = 0, len(nums)-1
    while l<=r:
        m = (l+r) // 2
        if nums[m] == m:
            return m
        elif nums[m] > m:
            r = m-1
        else:
            l = m
    return False