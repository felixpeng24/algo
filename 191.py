"""
Given a collection of intervals, 
find the minimum number of intervals you need to remove to make 
the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], 
but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), 
return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.

"""
#what if we did sort the intervals?
#this feels like dp, but im not sure if thats the case: like removing 

#sort by last number since we want each interval to leave more room for the others

def removeInterval(nums):
    nums.sort(key= lambda x: x[1])

    count = 0
    last_end = float('-inf')
    for num in nums:
        if num[0] >= last_end:
            last_end = num[1]
        else:
            count += 1
    return count

