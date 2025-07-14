"""
You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.

"""

def push_dominoes(s):
    n = len(s)
    left = [0] * n
    right = [0] * n

    # Rightward force
    force = 0
    for i in range(n):
        if s[i] == 'R':
            force = n
        elif s[i] == 'L':
            force = 0
        else:
            force = max(force - 1, 0)
        right[i] = force

    # Leftward force
    force = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            force = n
        elif s[i] == 'R':
            force = 0
        else:
            force = max(force - 1, 0)
        left[i] = force

    # Resolve forces
    result = []
    for l, r, c in zip(left, right, s):
        if l == r:
            result.append('.' if l == 0 else c)
        elif l > r:
            result.append('L')
        else:
            result.append('R')

    return ''.join(result)
