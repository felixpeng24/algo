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

Write a function is_palindrome() that takes in a string s as a parameter and returns True if the string is a palindrome and False otherwise. 
You may assume the string contains only lowercase alphabetic characters.

input: "kayak"
output: True

word drow

racecar racecar

kayyak

input: "kaak"
output: True

def is_palindrome(s):
    l = 0
    r = len(s)-1
    
    while l<r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    
    return True



Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
# initialize empty list called nums
# initialize a dict
    # key : value
    # val : valIdx

bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# check if the val is not present in numMap
    # add val into numArr (append)
    # add val into numMap
        self.numMap[val]= len(self.numArr)-1
    # return True
# return False


idx = self.numMap[val]
# [3,6,8,7]

# {3:0, 6:1, 2:2}
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# check if the val is present in numMap
    # del val from numMap
        numMap.remove[]
    # del val from numArr
    self.numSet.remove(val)
    # return True
# return False

int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# return numArr[random number from size of list]
                                                                                                          
You must implement the functions of the class such that each function works in average O(1) time complexity.
                                                                           
import random
class RandomizedSet(object):
    def __init__(self):

    def insert(self, val):                                                                                                                             

    def remove(self, val):
                                                                
    def getRandom(self):
                                                                           


    