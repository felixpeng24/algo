"""
Given a circular array, compute its maximum subarray sum in O(n) time.
A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 
where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
"""

#o(n) so cant brute force by going through every number
#maybe a two pointer method? where a right point can be moved to the left of left pointer

def maxSubarraySumCircular(nums):
    # Function to apply Kadane's algorithm to find maximum subarray sum
    def kadane(arr):
        max_ending_here = max_so_far = 0  # sum starts at 0 for empty subarray
        for num in arr:
            max_ending_here = max(0, max_ending_here + num)  # reset if negative
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Step 1: Compute the max subarray sum for the non-circular case
    max_kadane = kadane(nums)

    # Step 2: Compute the max subarray sum for the circular case
    total_sum = sum(nums)
    # Negate all elements of nums
    neg_nums = [-x for x in nums]
    # Kadane's algorithm on the negated array gives the minimum subarray sum
    min_kadane = kadane(neg_nums)
    
    # Step 3: Calculate the circular subarray sum
    max_circular = total_sum + min_kadane  # because min_kadane is negative
    
    # If all elements are negative, circular subarray is not possible
    if max_circular == 0:
        return max_kadane
    else:
        return max(max_kadane, max_circular)

# Example usage:
print(maxSubarraySumCircular([8, -1, 3, 4]))  # Output: 15
print(maxSubarraySumCircular([-4, 5, 1, 0]))  # Output: 6
