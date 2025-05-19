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