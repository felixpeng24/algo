"""
This problem was asked by Netflix.

Given a sorted list of integers of length N, determine if an element x is in the list without performing any multiplication, division, or bit-shift operations.

Do this in O(log N) time.


"""
#bruh is it not just binary search???

def bs(nums, x):
    l, r = 0, len(nums) - 1
    while l<r:
        m = (l+r) // 2
        if nums[m] == x:
            return True
        elif nums[m] > x:
            r = m - 1
        else:
            l = m + 1
    return False

#no division
#pointers at left
#right pointer same location, increase index by powers of two until it poitns at number greater
#left pointer 
#wait we only need one
# 1, 2, 4, 8, 16

def bsBetter(nums, x):
    step_size = []
    s = 1
    while s <= len(nums):
        step_size.append(s)
        s += s
    step_ptr = len(step_size) - 1
    l = step_size[step_ptr]
    while step_ptr >= 0:
        if x == nums[l]:
            return True
        elif nums[l] > x:
            step_ptr -= 1
            l -= step_size[step_ptr]
        else:
            step_ptr -= 1
            l += step_size[step_ptr]

    
    return False


# Element exists in middle
nums = [1, 3, 5, 7, 9]
x = 5  # Expected: True
print(bsBetter(nums, x))
# Element exists at beginning
nums = [2, 4, 6, 8, 10]
x = 2  # Expected: True
print(bsBetter(nums, x))
# Element exists at end
nums = [2, 4, 6, 8, 10]
x = 10  # Expected: True
print(bsBetter(nums, x))
# Target less than min
nums = [5, 10, 15]
x = 1  # Expected: False
print(bsBetter(nums, x))
# Target between elements
nums = [1, 3, 5, 7]
x = 6  # Expected: False
print(bsBetter(nums, x))
# Target greater than max
nums = [10, 20, 30]
x = 35  # Expected: False
print(bsBetter(nums, x))
# Empty list
nums = []
x = 1  # Expected: False
print(bsBetter(nums, x))
# Single-element list, match
nums = [7]
x = 7  # Expected: True
print(bsBetter(nums, x))
# Single-element list, no match
nums = [7]
x = 3  # Expected: False
print(bsBetter(nums, x))

