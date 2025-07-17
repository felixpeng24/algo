"""
1. Given a string print all subsets (not permutations)

Eg. String "abc" should output
"abcd"
empty string
a
b
c
d
ab
ac
ad
bc
bd
cd
abc
abc

"""

#does order matter?

# def subsets(s):
#     if len(s) == 1:
#         return s
#     for i in range(len(s[1:])):
#         return s[i] + subsets(s[i:])
    
# print(subsets("abc"))



def generate_subsets(s):
    def backtrack(index, path):
        if index == len(s):
            print(''.join(path))
            print("test")
            return
        # Exclude first
        backtrack(index + 1, path)
        # Include
        path.append(s[index])
        backtrack(index + 1, path)
        path.pop()

    backtrack(0, [])

generate_subsets("abc")