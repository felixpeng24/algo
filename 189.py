"""
Given an array of elements, return the length of the longest 
subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], 
return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

Easy
"""

#we do kadanes algorithm again?
#sliding window using a set


# problem with this is that we dont accunt for something like
# 543215467890
#maybe a two pointer sliding window method again, instead of kadanes wihcih is used for sum finding

"""  numSet = set()
    overallMax = currMax = 0
    for num in nums:
        if num not in numSet:
            currMax += 1
            overallMax = max(currMax, overallMax)
            numSet.add(num)
        else:
            overallMax = max(currMax, overallMax) """



def distinctsubArray(nums):
    seen = {}
    l = 0
    max_len = 0
  #  for right in range(len(nums)):


def longest_distinct_subarray(nums):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            left += 1
        seen.add(nums[right])
        max_len = max(max_len, right - left + 1)

    return max_len


print(longest_distinct_subarray([5,1,2,3,4,4,6,7,8,9,0,11,12,13]))


#remove one at a time while right is still in seen, ohhhh makes sense with sliding window
# no need to cut through in the middle



    