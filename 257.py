"""
easy
This problem was asked by WhatsApp.

Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order 
for the entire array to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1, 3).

"""

#oh thats interesting, i wonder if this is a two pointer problem based on the bounds, and we slowly decrease each bound until it doesnt matter anymore? but 
# then its be n^2logn right?

#so look at min max where order breaks, and use that to adjust boundaries
# so for [3, 7, 5, 6, 9, we see that order breaks at 7, 5
#start from left,, when can 5 fit in? at (1, x)
#start from right, where can 7 fit in? at (x, 3)
#return (1, 3)

#Test Case:
#[1, 2, 6, 5, 4, 3, 7, 8]
#order breaks, min being 3, max being 6
#start from left,, when can 3 fit in? at (2, x)
#start from right, where can 6 fit in? at (x, 3)
#return (1, 3)

def find_unsorted_window(arr):
    sorted_arr = sorted(arr)
    start = 0
    while start < len(arr) and arr[start] == sorted_arr[start]:
        start += 1

    end = len(arr) - 1
    while end > start and arr[end] == sorted_arr[end]:
        end -= 1

    return (start, end) if start < end else (-1, -1)
