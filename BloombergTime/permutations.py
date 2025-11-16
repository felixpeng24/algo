"""

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

def numPermutations(nums):
    #go through each num, choice to include or exlcude, add to res list once we reach end
    #helper function, pass thorugh the index we r on, and our curr set
    res = []
    def backtrack(idx, curr:list):
        if idx == len(nums):
            res.append(curr)
            return
        #exclude
        backtrack(idx+1, curr)
        #include
        backtrack(idx+1, curr+[nums[idx]])
    backtrack(0, [])
    
    return res



#mutable

def mutableSubsets()
print(numPermutations([1,2,3]))

