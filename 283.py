"""
A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.



"""

# 2 3 5, 
# 2, 3, 22 4, 5, 23 6, 222 8, 33 9, 25 10, 223 12  
#could we binary it, and use it as digits? nope
#min heap, pop root, or three pointers, one for each of regulars(i2)

import heapq

def minheap(n):
    heap = []
    seen = set()
    heapq.heappush(heap, 1)
    while n>0:
        curr = heapq.heappop(heap)
        print(curr)
        n -= 1
        for factor in [2, 3, 5]:
            new = curr * factor

            if new not in seen:
                heapq.heappush(heap, new)
                seen.add(new)
        
    return

print(minheap(12))

def threeptr(n):
    regulars = [1]
    i2, i3, i5, = 0, 0, 0
    while len(regulars) < n:
        
    for num in regulars:
        print(num)
    
    return


def regular_numbers(n):
    regulars = [1]
    i2 = i3 = i5 = 0  # pointers

    while len(regulars) < n:
        next2 = regulars[i2] * 2
        next3 = regulars[i3] * 3
        next5 = regulars[i5] * 5

        next_val = min(next2, next3, next5)
        regulars.append(next_val)

        # Increment pointers for whichever produced the min
        if next_val == next2:
            i2 += 1
        if next_val == next3:
            i3 += 1
        if next_val == next5:
            i5 += 1

    return regulars