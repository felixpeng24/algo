# 1
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Try to do in O(n)

def max_non_adjacent_sum(nums):
    if not nums:
        return 0

    include = 0  # Sum including the current number
    exclude = 0  # Sum excluding the current number

    for num in nums:
        new_include = exclude + num  # Include current number
        exclude = max(include, exclude)  # Exclude current number
        include = new_include  # Update include to new value
    
    return max(include, exclude)
