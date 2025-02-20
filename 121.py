"""
Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
"""

#pointer at the ends

def is_removable_palindrome(s, k):
    l, r = 0, len(s)-1
    # for the example of like "qqqqqqracecar"
    if s[l] != s[r]:
