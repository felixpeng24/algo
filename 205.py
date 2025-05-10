"""
Given an integer, find the next permutation of it in absolute order. 
For example, given 48975, the next permutation would be 49578.

similar to counting up in binary, except digits represent what base system we are using
4 5 7 8 9
0 0 0 0 0

4 5 7 9 8

would be start?
but then adding a one would be 

For example, for 123, all permutations are:

123, 132, 213, 231, 312, 321

1234 1243 1324 1342 1423 1432

for 1:

1 + recurse (2, 3)
1+ 3, 2

given string of num, output list of all permutations
"""

# def perms(num):
#     permList = []
#     def recurse(numstr):
#         if len(numstr) == 2:
#             return [numstr, numstr[::-1]]
        
#         for num in numstr:
#             permList += [num + f for f in recurse(numstr[1:])]
    
def get_permutations(s):
    if len(s) == 1:
        return [s]

    perms = []
    for i in range(len(s)):
        current = s[i]
        remaining = s[:i] + s[i+1:]
        for p in get_permutations(remaining):
            perms.append(current + p)
    return perms

# Example usage:
num = "123"
result = get_permutations(num)
print(result)

        
    

num = "123"