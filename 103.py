"""
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.

"""

# sliding window?

def in_substring(substr, d):
    for s in substr:
        if s in d:
            d.remove(s)
    if len(d) == 0:
        return True
    else:
        return False


def substring(s, d):
    l = 0

    for r in range(1, len(s)+1):
        while r-l > len(d) and l<r:
            l += 1
        if substring(s[l:r],d):
            return s[l:r]
