"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.

[7 10 3 4 5]

[3 4 5 6 7 ]
"""


def minElement(nums):
    l, r = 0, len(nums)-1
    while l<r:
        m = (l + r) // 2
        if nums[m]>nums[l]:
            l = m+1
        else:
            r = m
    
    return nums[l]

nums = [5, 7, 10, 3, 4]

print(minElement(nums))

