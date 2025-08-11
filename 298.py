"""
A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.

"""
from collections import defaultdict
def uniqueApple(apples):
    appleHash = defaultdict(int)
    l,r = 0, 1
    appleHash[apples[0]] += 1
    appleHash[apples[1]] += 1
    maxPortion = 2
    while r < len(apples):
        r += 1
        if apples[r] in appleHash:
            appleHash[apples[r]] += 1
            maxPortion = max(maxPortion, r - l + 1)
        else:
            while 
    
    return maxPortion
