"""
Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
"""

#pointer at the ends

from functools import lru_cache

def can_make_palindrome(s: str, k: int) -> bool:
    @lru_cache(None)  # Memoization
    def helper(left: int, right: int, k: int) -> bool:
        if left >= right:
            return True  # Base case: single character or empty substring is a palindrome
        if s[left] == s[right]:
            return helper(left + 1, right - 1, k)  # Move inward if characters match
        if k > 0:
            return helper(left + 1, right, k - 1) or helper(left, right - 1, k - 1)  # Try deleting either side
        return False  # Exceeded deletion limit

    return helper(0, len(s) - 1, k)

# Example usage:
print(can_make_palindrome("waterrfetawx", 2))  # Output: True
