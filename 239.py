"""
One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.

"""

def number_of_patterns(n):
    jumps = [[0] * 10 for _ in range(10)]
    jumps[1][3] = jumps[3][1] = 2
    jumps[1][7] = jumps[7][1] = 4
    jumps[3][9] = jumps[9][3] = 6
    jumps[7][9] = jumps[9][7] = 8
    jumps[1][9] = jumps[9][1] = 5
    jumps[3][7] = jumps[7][3] = 5
    jumps[2][8] = jumps[8][2] = 5
    jumps[4][6] = jumps[6][4] = 5
    jumps[5][5] = 0

    def dfs(visited, curr, remaining):
        if remaining == 0:
            return 1
        total = 0
        visited[curr] = True
        for next in range(1, 10):
            jump = jumps[curr][next]
            if not visited[next] and (jump == 0 or visited[jump]):
                total += dfs(visited, next, remaining - 1)
        visited[curr] = False
        return total

    total_patterns = 0
    visited = [False] * 10
    for length in range(n, n + 1):
        total_patterns += dfs(visited, 1, length - 1) * 4  # corners
        total_patterns += dfs(visited, 2, length - 1) * 4  # edges
        total_patterns += dfs(visited, 5, length - 1)      # center
    return total_patterns
