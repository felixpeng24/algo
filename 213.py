"""
Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. 
Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].

"""

# instead of going from the front, we start from back? guess it doesnt matter, we cant overflow with 255
# recursive problem where we start from ABCD, to BCD, to CD, to D? seems pretty inefficient
#so what we know is cant start with 3 or more
# im thinking recursion too....

# base case: if input is empty, return ""

# candidate statements would look something like:

# fiurst scenario: keep appending digits until the next digit is 2 or less (cant be greater than 255)
# append combinations of the amount of digits we can play with, (so with a string of 1234 left, we use a 1, a 12, a 123, but not a 1234)

#backtracking is the play here, we have a multiple drcision trees with the root being the first A in the IP address, and the trees are pretty hugde
# so what does last leaf look like? well thered just be one option left riht?  there are certain branches of the tree that need to be thrown away as well

#so base case checks: if there are four segments AND: 0 numbers left, add onto list, some numbers left, do nothing
#so our recrusive function has two parameters, # of segments and remaining string left...i dont see the backtracking part of this yet


def IPcombo(nums): #nums is a string
    res = []
    def isValid(segment):
        if segment == "0":
            return True
        elif len(segment) > 1 and segment[0] == "0":
            return False
        elif int(segment) <= 255:
            return True
        else:
            return False

    def backtrack(path, remaining): 
    #path is the current path represented by a list of segments, remianing is a string of reamining nums, and segment is number of segments right now we're on
        if (len(path) == 4 and len(remaining) != 0) or (len(path) != 4 and len(remaining) == 0):
            return
        if len(path) == 4 and len(remaining) == 0:
            final = '.'.join(path)
            res.append(final)
        for i in range(min(len(remaining), 3)):
            currSegment = remaining[:i+1]
            if isValid(currSegment):
                path.append(currSegment)
                backtrack(path, remaining[i+1:])
                path.pop()
    
    backtrack([], nums)
    
    return res

    
print(IPcombo("25525511135"))
# Expected: ['255.255.11.135', '255.255.111.35']

print(IPcombo("0000"))
# Expected: ['0.0.0.0']

print(IPcombo("1111"))
# Expected: ['1.1.1.1']

print(IPcombo("101023"))
# Expected: ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']



