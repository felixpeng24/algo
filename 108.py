"""
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.

"""

#shift by k from cs newsletter, check each variant? brute force solution?

def shiftable(a, b):

    def shift(a, k):
        # shift a by k
        # abcde, k=2, deabc ----- double reverse/in place?
        a = list(a)
        l, r = 0, len(a)-1
        while l<r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
            # edcba
        l, r = 0, k-1
        while l<r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        l, r = k, len(a)-1
        while l<r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        return "".join(a)
    
    for k in range(len(a)):
        if shift(a, k) == b:
            return True
    
    return False

a = "abcde"
b = "cdab"
print(shiftable(a,b))