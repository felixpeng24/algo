"""
Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?

"""

"""
right to left

i = 3 (building row 3):

j=3: row[3] = 0 + 1 = 1
j=2: row[2] = 1 + 2 = 3
j=1: row[1] = 2 + 1 = 3
[1, 3, 3, 1, 0]

"""


def get_row(k):
    row = [0] * (k + 1)
    row[0] = 1  # First element always 1

    for i in range(1, k + 1):
        for j in range(i, 0, -1):  # Update from right to left
            row[j] += row[j - 1]

    return row

# Example:
print(get_row(4))  # [1, 4, 6, 4, 1]
