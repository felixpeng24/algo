"""
Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g
"""

def print_zigzag(s, k):
    if k == 1:
        print(s)
        return

    # Prepare rows
    rows = ['' for _ in range(k)]
    curr_row = 0
    direction = 1  # 1 means down, -1 means up

    # Fill rows
    for char in s:
        rows[curr_row] += char
        for i in range(k):
            if i != curr_row:
                rows[i] += ' '  # pad with space to keep alignment

        curr_row += direction
        if curr_row == 0 or curr_row == k - 1:
            direction *= -1

    # Print the zigzag pattern
    for row in rows:
        print(row)

# Example
print_zigzag("thisisazigzag", 4)

#def a way to do mathematically as well

def print_zigzag_math(s, k):
    if k == 1:
        print(s)
        return

    n = len(s)
    cycle_len = 2 * k - 2
    rows = ['' for _ in range(k)]

    # Build each row mathematically
    for r in range(k):
        i = r
        while i < n:
            rows[r] += ' ' * (i - len(rows[r])) + s[i]  # align spacing
            if 0 < r < k - 1:
                j = i + cycle_len - 2 * r  # the diagonal part
                if j < n:
                    rows[r] += ' ' * (j - len(rows[r])) + s[j]
            i += cycle_len

    for row in rows:
        print(row)

print_zigzag_math("thisisazigzag", 4)
