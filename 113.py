"""
Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

Triple Follow up:

Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. 
For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""

# two pointers and detect the space? or make extra space using a list, reversing the list using pointers, then outputing with extra space in between?