"""

Given a set of distinct positive integers, 
find the largest subset such that every pair of elements in the subset 
(i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. 
Given [1, 3, 6, 24], return [1, 3, 6, 24].
"""

#brute force?
#no ofc its dp its always dp
    # we have a dp list containing number of combos that can be made, but still double for loops
    # and a prev list containing all the indicies


def largestDivisibleSubset(nums):
    if not nums:
        return []

    nums.sort()
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    max_index = 0

    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[i] > dp[max_index]:
            max_index = i

    # Reconstruct the subset
    result = []
    while max_index != -1:
        result.append(nums[max_index])
        max_index = prev[max_index]

    return result[::-1]

# dp[i]: The size of the largest divisible subset that ends at index i (with nums[i] as the largest number in the subset)

# prev[i]: The index of the previous element in the subset that leads to nums[i]

#this is insanity

r"""
nums = [3, 5, 10, 20, 21]
🔢 Step 1: Sort the Input
python
Copy
Edit
nums = [3, 5, 10, 20, 21]
→ After sorting:

python
Copy
Edit
nums = [3, 5, 10, 20, 21]
(Note: already sorted)

📦 Step 2: Initialize DP Arrays
We create two arrays:

dp = [1, 1, 1, 1, 1] — every element is a subset of size 1 by itself

prev = [-1, -1, -1, -1, -1] — no previous element yet

🔁 Step 3: Fill DP and Prev
We check each pair nums[j], nums[i] where j < i, and update if divisible:

i = 1 (nums[1] = 5)
j = 0: 5 % 3 ≠ 0 → skip

➡️ dp = [1, 1, 1, 1, 1], prev = [-1, -1, -1, -1, -1]

i = 2 (nums[2] = 10)
j = 0: 10 % 3 ≠ 0 → skip

j = 1: 10 % 5 == 0 → valid, dp[2] = dp[1] + 1 = 2, prev[2] = 1

➡️ dp = [1, 1, 2, 1, 1], prev = [-1, -1, 1, -1, -1]

i = 3 (nums[3] = 20)
j = 0: 20 % 3 ≠ 0 → skip

j = 1: 20 % 5 == 0 → dp[3] = dp[1] + 1 = 2, prev[3] = 1

j = 2: 20 % 10 == 0 → dp[2] = 2, so dp[3] = dp[2] + 1 = 3, prev[3] = 2

➡️ dp = [1, 1, 2, 3, 1], prev = [-1, -1, 1, 2, -1]

i = 4 (nums[4] = 21)
j = 0: 21 % 3 == 0 → dp[4] = dp[0] + 1 = 2, prev[4] = 0

j = 1: 21 % 5 ≠ 0

j = 2: 21 % 10 ≠ 0

j = 3: 21 % 20 ≠ 0

➡️ dp = [1, 1, 2, 3, 2], prev = [-1, -1, 1, 2, 0]

🧮 Step 4: Find Max
Max of dp is 3 at index 3 → nums[3] = 20

🔁 Step 5: Reconstruct Subset
Follow prev backward from index 3:

20 (index 3)

10 (index 2)

5 (index 1)

➡️ [20, 10, 5] → reverse → [5, 10, 20]


"""