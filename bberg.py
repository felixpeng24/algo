"""

Given a string print all subsets (not permutations)

Eg. String "abc" should output
empty string
a
b
c
ab
bc
ac
abc
"""

def string_output(s):
    for l in range(len(s)):
        for i in range(len(s)):
            print(s[l:i+1])


def generate_subsets(s, index=0, current=""):
    if index == len(s):
        print(current)
        return
    
    # Exclude the current character
    generate_subsets(s, index + 1, current)
    
    # Include the current character
    generate_subsets(s, index + 1, current + s[index])

# Example usage

def iteration_subsets(s):
    subsets = [""]

    for letter in s:
        new_subset = []
        for subset in subsets:
            new_subset.append(subset + letter)
        
        subsets.extend(new_subset)
    
    print(subsets)

iteration_subsets("abcd")

