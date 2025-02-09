"""
238. Product of Array. Except Self. Given an integer array nums, return an array answer such that answer [i] is equal to the product of all the elements of nums except nums [i].
CS Newsletter


SS for boba raffle? 

[a,b,c,d,e]
[bcde, acde, abde, abce, abcd]
pre: [1, a, ab, abc, abcd]
post: [bcde, cde, de, e, 1]


"""

def productOfArray(nums):
    result = [1] * len(nums)
    post = 1
    for i in range(len(nums)):
        k = 0
        while k < i:
            result[i] *= nums[k]
            k += 1
    for i in range(len(nums)):
        i = -i-1
        result[i] *= post
        post *= nums[i]
    return result

test = [2,3,4,5] # [60, 40, 30, 24]

print(productOfArray(test))


