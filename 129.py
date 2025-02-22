"""

Given a real number n, find the square root of n. For example, given n = 9, return 3.

"""

# binary search? start from 1, so itself, then cut by half

def sqrroot(n):
    if n < 0:
        return "Nah"
    l, r = 0, n
    curr = n
    while curr ** 2 != n:
        if curr ** 2 > n:
            curr = (l + r) // 2
            r = curr
        else:
            curr = (l+r)//2
            l = curr

    
    return curr

print(sqrroot(16))