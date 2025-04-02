"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. 
daily should return false, since there's no rearrangement that can form a palindrome.

"""

# easy? check if it has the right combo of letters through hasmap

from collections import Counter

def can_form_palindrome(s):
    char_counts = Counter(s)
    odd_count = sum(1 for count in char_counts.values() if count % 2 == 1)
    return odd_count <= 1

# Test cases
print(can_form_palindrome("carrace"))  # True
print(can_form_palindrome("daily"))    # False
