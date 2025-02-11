"""
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""


def sqrsort(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    nums.sort()
    return nums

"""
doesnt work since num doesnt change the actual value inside of nums

def sqrsort(nums):
    for num in nums:
        num = num**2
    nums.sort()
    return nums

"""
nums = [-9, -2, 0, 2, 3]
 #print(sqrsort(nums))

 def sqrsortptr(nums):
   
