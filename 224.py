"""
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.

easy

"""

#going throuhg every number and brute forcing it? nah this would be m*n complexity
#and we can assume the firsy numebr is always 1, otherwise we return 1
#o(n) ius a hint, we need possible one for loop and iterate through all the numbers
#and it being sorted is another hint? where does binary search come into play?
#we have numSet to have all the sums we can make, and start with 1. add to set. now look at 2. add to set, and add to 1 to get three which we add to the set. repeat with 3...etc. am i going in the right direction

#what if multiple holes? cant make 7 but can make 8 and the next number is 8 or smthg