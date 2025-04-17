"""
Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].

"""
"nnnnnnn"   "n", "n", "n"  
#as few strings as possible, so something like nnnnnnn would be by itself
# start from out to in, left pointer and right, check if similar letters? then delete that one and continue
# greedy approach doesnt work, seems that when greedy fails dp is used
# counterex: sabasdfghgfdsas
# greedy would say aba, sdfds, a
# dp would do a, b, 

def isPalindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def substringer(s):
    l, r = 0, len(s) - 1
    res = []
    while len(s) > 0:
        if not isPalindrome(s, l, r):
            r -= 1
        else:
            res.append(s[l:r+1])
            s = s[r+1:]
            l, r = 0, len(s)-1
    return res

print(substringer("sabasdfghgfdsas"))


# GPT's solution

def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def min_palindrome_partition(s):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # No cuts needed for an empty string

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(i):
            if is_palindrome(s, j, i - 1):
                dp[i] = min(dp[i], dp[j] + 1)

    # Reconstruct palindromes from DP table
    result = []
    i = n
    while i > 0:
        for j in range(i):
            if is_palindrome(s, j, i - 1) and dp[i] == dp[j] + 1:
                result.append(s[j:i])
                i = j
                break

    return result[::-1]  # Reverse to get the correct order

# Example usage:
print(min_palindrome_partition("racecarannakayak"))  # Output: ['racecar', 'anna', 'kayak']
print(min_palindrome_partition("abc"))  # Output: ['a', 'b', 'c']
