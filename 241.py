"""
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.

# [0 1 3 4 5]


"""

def citation(nums):
    nums.sort()
    # for reverse_i in range(len(nums)):
    #     i = len(nums) - 1 - reverse_i
    #     if nums>
    #         return reverse_i+1
    for i in range(len(nums)):
        if nums[i] >= len(nums)-1:
            return len(nums)

def calculate_h_index(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h

# Example usage
citations = [4, 3, 0, 1, 5]
print(calculate_h_index(citations))  # Output: 3

nums = [10, 10, 10, 10, 10] 
nums = [4, 3, 0, 1, 5] 
print(citation(nums))






    