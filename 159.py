"""
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

"""

# hash set

def first_recurring_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char  # First recurring character found
        seen.add(char)
    return None  # No recurring character

# Example usage:
print(first_recurring_char("acbbac"))  # Output: "b"
print(first_recurring_char("abcdef"))  # Output: None
