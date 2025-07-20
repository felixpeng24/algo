"""

The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""

def look_and_say(N):
    term = "1"
    for _ in range(N - 1):
        next_term = ""
        i = 0
        while i < len(term):
            count = 1
            # Count consecutive identical digits
            while i + 1 < len(term) and term[i] == term[i + 1]:
                i += 1
                count += 1
            next_term += str(count) + term[i]
            i += 1
        term = next_term
    return term

# Example usage:
N = 5
print(look_and_say(N))  # Output: 111221
