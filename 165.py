"""

Given an array of integers, return a new array where each element in the new array is 
the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""

# could do boring n^2 solution with brute force?

from bisect import bisect_left

def count_smaller_elements(nums):
    sorted_nums = sorted(set(nums))  # Get unique sorted values
    bit = [0] * (len(sorted_nums) + 1)
    
    def update(index, value):
        while index < len(bit):
            bit[index] += value
            index += index & -index

    def query(index):
        total = 0
        while index > 0:
            total += bit[index]
            index -= index & -index
        return total

    result = []
    for num in reversed(nums):
        idx = bisect_left(sorted_nums, num)
        result.append(query(idx))
        update(idx + 1, 1)

    return result[::-1]

# Example usage:
print(count_smaller_elements([3, 4, 9, 6, 1]))  # Output: [1, 1, 2, 1, 0]
