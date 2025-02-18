"""
Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   
 5      15
       /  
     11    15
Return the nodes 5 and 15.

"""

#two pointer method sinc eit is specifically twopointer? move left and right depending on whather or not it should be less or more
#if current sum less, move right? but when would we move left since the number of pointers would increase as we go down