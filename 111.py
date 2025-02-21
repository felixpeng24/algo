"""
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""
#hard
#check for anagrams usually using a hashmap
#start with helper function of anagram checker

from collections import Counter

def find_anagram_indices(W, S):
    w_len = len(W)
    s_len = len(S)
    result = []
    
    if w_len > s_len:
        return result
    
    # Frequency dictionary of W
    w_count = Counter(W)
    
    # Initial window frequency dictionary
    window_count = Counter(S[:w_len])
    
    # Check first window
    if window_count == w_count:
        result.append(0)
    
    # Slide the window
    for i in range(1, s_len - w_len + 1):
        # Remove the leftmost character
        left_char = S[i - 1]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]  # Remove key to avoid unnecessary comparisons
        
        # Add the rightmost character
        right_char = S[i + w_len - 1]
        window_count[right_char] += 1
        
        # Compare window with W
        if window_count == w_count:
            result.append(i)
    
    return result

# Example usage
W = "ab"
S = "abxaba"
print(find_anagram_indices(W, S))  # Output: [0, 3, 4]
