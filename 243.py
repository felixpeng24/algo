"""
Given an array of numbers N and an integer k, your task is to split N into 
k partitions such that the maximum sum of any partition is minimized. Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, 
since the optimal partition is [5, 1, 2], [7], [3, 4].

"""
#brute force is trying to partition it at all locations
#Given a candidate max partition sum (say mid),
#can you simulate walking through the array and counting how many partitions you’d need if no partition exceeds mid?

def helper(nums, mid):
    partitions = 1
    curr_sum = 0
    for num in nums:
        if curr_sum + num > mid:
            curr_sum = num
            partitions += 1
        else:
            curr_sum += num
    return partitions

def partitioner(N, k):
    l = max(N)
    r = sum(N)

    while l<r:
        mid = (l+r)//2
        if helper(N, mid) <= k:
            r = mid
        else:
            l = mid + 1
    return l

N = [5, 1, 2, 7, 3, 4]
k = 3
print(partitioner(N, k))