"""
Hard


Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:

[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]
And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the
matrix smaller than 6 or greater than 23.

"""

#when sorted, binary search becomes an option:

def count_smaller(matrix, target):
    # Count elements strictly less than target
    count = 0
    n = len(matrix)
    m = len(matrix[0])
    row, col = n - 1, 0
    while row >= 0 and col < m:
        if matrix[row][col] < target:
            count += row + 1  # All rows above this one also < target
            col += 1
        else:
            row -= 1
    return count

def count_greater(matrix, target):
    # Count elements strictly greater than target
    count = 0
    n = len(matrix)
    m = len(matrix[0])
    row, col = 0, m - 1
    while row < n and col >= 0:
        if matrix[row][col] > target:
            count += m - col  # All columns to the right also > target
            row += 1
        else:
            col -= 1
    return count

def count_smaller_and_greater(matrix, i1, j1, i2, j2):
    val1 = matrix[i1][j1]
    val2 = matrix[i2][j2]
    return count_smaller(matrix, val1) + count_greater(matrix, val2)

# Example usage
matrix = [
    [1, 3, 7, 10, 15, 20],
    [2, 6, 9, 14, 22, 25],
    [3, 8, 10, 15, 25, 30],
    [10, 11, 12, 23, 30, 35],
    [20, 25, 30, 35, 40, 45]
]

i1, j1 = 1, 1
i2, j2 = 3, 3

print(count_smaller_and_greater(matrix, i1, j1, i2, j2))  # Output: 15
