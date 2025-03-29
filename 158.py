"""
This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, 
how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a 
wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

"""
#keep going right, then down 1, then all the way right on 1st iteration
#remember # of steps, then subtract 1 from the first right to go down 1 a step earlier, repeat for the rest