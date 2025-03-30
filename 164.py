"""
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. 
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.

"""

#dont we just add to dictionary and find?

def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1  # This should never happen given the problem constraints.

# Example usage:
nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))  # Output: 2

def find_duplicate(nums):
    # Phase 1: Detect cycle
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    # Phase 2: Find entry point of cycle (duplicate number)
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# Example usage:
nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))  # Output: 2
