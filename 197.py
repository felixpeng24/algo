"""

This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the array,
 rotate the array to the right k elements in-place.


"""

# [0 1 2 3 4 5] k=3, [345012]


def rotate(nums, k):
    return nums[len(nums) - k:] + nums[:len(nums) - k]

def rotateInPlace(nums, k):
    def reverseME(nums):
        l = 0
        r = len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
    
    numss = reverseME(nums)
    reverseME(numss[:k])
    reverseME(numss[k:])
    return numss


nums = [0, 1, 2, 3, 4, 5]
k = 3
print(rotateInPlace(nums, k))

#slicing makes a copy