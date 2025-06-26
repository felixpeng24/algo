"""
palantir easy

The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. 
For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.

"""
#how did they get 4, 18, and 468
#how about increasing??
"""
like go down the list of 1/, 1/3, 1/4, and the moment it works we subtract, adn go downt he list

"""

def egypt(num):
    denominator = 2
    res = []
    while num > 0:
        if num < (1 / denominator):
            denominator += 1
        else:
            num -= (1 / (denominator))
            res.append(denominator)
    return res

print(egypt(4/13))