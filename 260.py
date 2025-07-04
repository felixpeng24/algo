"""
This problem was asked by Pinterest.

The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order is an array representing whether each number 
is larger or smaller than the last. Given this information, reconstruct an array that is consistent with it. For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4]

"""

def reconstruct_from_directions(directions):
    n = len(directions)
    res = []
    stack = []

    for i in range(n):
        stack.append(i)
        # If it's the end or the next comparison is '+', flush the stack
        if i == n - 1 or directions[i + 1] == '+':
            while stack:
                res.append(stack.pop())
    
    return res
