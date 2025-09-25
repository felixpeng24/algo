"""
Given an array of numbers and a number k, determine if there are three entries in the array 
which add up to the specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.
#ptr left ptr right side, shift if less than or greater, sort
"""

def three_sum(nums, k):
    nums.sort()  # Step 1: sort
    n = len(nums)
    
    for i in range(n - 2):  # Fix one element
        left, right = i + 1, n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == k:
                return True  # Found a triplet
            elif total < k:
                left += 1
            else:
                right -= 1
    
    return False  # No triplet found


# Example usage
print(three_sum([20, 303, 3, 4, 25], 49))  # True (20 + 4 + 25 = 49)
