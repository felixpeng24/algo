"""
Implement an efficient string matching algorithm.

That is, given a string of length N and a pattern of length k, write a program that searches 
for the pattern in the string with less than O(N * k) worst-case time complexity.

If the pattern is found, return the start index of its location. If not, return False

"""

def kmp_search(text: str, pattern: str):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix

        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    if not pattern:
        return 0  # empty pattern matches at index 0

    lps = build_lps(pattern)
    i = j = 0  # i for text, j for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            return i - j  # match found
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False  # no match found
