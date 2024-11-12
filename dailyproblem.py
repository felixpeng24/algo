# 1
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Try to do in O(n)

def max_non_adjacent_sum(nums):
    if not nums:
        return 0

    include = 0  # Sum including the current number
    exclude = 0  # Sum excluding the current number

    for num in nums:
        new_include = exclude + num  # Include current number
        exclude = max(include, exclude)  # Exclude current number
        include = new_include  # Update include to new value
    
    return max(include, exclude)

# testing the add and commit stuff rn

def add(a, b):
    return a+b

#Wondering if I can just save locally with ctrl+s and then push

def subtract(a, b):
    return a-b

#interesting didnt update
#alright guess i gotta do all three
# git add, git commit -m "commit msg", git push origin main


nums = [3,7,11,2]
target = 9
print(enumerate(nums))

def twoSum(nums, target):
    hashmap = {}
    i = 0
    for num in nums:
        hashmap[num] = i
        i += 1
        if (target - num) in hashmap:
            return [hashmap[target - num], hashmap[num]]

print(twoSum(nums, target))

# bracket map
def for_bracket(s):
    if s[0] == "}" or s[0] == "]" or s[0] == ")":
        return False
    open_bracket = 0
    open_curly = 0
    open_parens = 0
"""    for bracket in s:
        if bracket == "{":
            open_bracket += 1
        if bracket == "}":
            
        if bracket == "[":
        if bracket == "]":
        if bracket == "(":
        if bracket == ")":
    return """

bracket_map = {')': '(', ']': '[', '}': '{'}

""" def bracket(s):
    stack = []
    pairs = {"{":"}", "[":"]", "(":")"}
    for char in s:
        if char in pairs.keys():
            stack += char
        elif char in pairs.values(): """


def is_balanced(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
    return not stack

def f(x,y):
    return x + 3*y

print(f(y=x,x=y))