"""
Write a program that computes the length of the longest common subsequence of three 
given strings. For example, given "epidemiologist", "refrigeration", and 
"supercalifragilisticexpialodocious", it should return 5, since the longest common subsequence is "eieio".

"""

#brute force is disgusting, going throuhg every posiibilituy of a subsequence would taker many years
# so we go dp?
#2d matrix, with each additonal word we update longest subsequence? but we cant take minimum like we did with coin change
#since addign an additonal word makes it more complex....what if we start off with two words

#try 2d table fiurst for just two words:


def LCS(A, B):
    dp = [[0] * (len(A)-1) for _ in range(len(B)) ]


A = "epidemiologist"
B = "refrigeration"
print(LCS(A, B))